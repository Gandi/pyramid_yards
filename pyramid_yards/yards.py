import logging

import colander
import translationstring
from functools import partial
from pyramid.session import check_csrf_token as check_csrf

log = logging.getLogger(__name__)
_ = translationstring.TranslationStringFactory('pyramid-yards')


class ValidationFailure(Exception):
    def __init__(self, errors):
        self.errors = errors


class Yards(object):
    """
    A place where http request parameter has been validated using colander.

    """

    def __init__(self, request):
        self._data = {}
        self.errors = {}
        self.attrs = {}

    def __call__(self, request):
        return self

    def __repr__(self):
        return repr(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __contains__(self, key):
        return key in self._data

    def keys(self):
        return self._data.keys()

    def items(self):
        return self._data.items()

    def get(self, key, default=None):
        return self._data.get(key, default)


class RequestSchema(object):
    def __init__(self, schema):
        self.schema = schema

    def validate(self, request, schema, filldict, prefix=''):
        for attr in schema.children:
            key = prefix + attr.name
            request.yards.attrs[key] = attr
            try:
                if hasattr(attr, 'location'):
                    data = getattr(request, attr.location)
                    val = attr.deserialize(data.get(key, attr.default))
                    if val != colander.drop:
                        filldict[attr.name] = val
                elif attr.children:
                    if isinstance(attr, colander.SequenceSchema):
                        val = attr.deserialize(data.getall(key) or
                                               attr.default)
                        if val != colander.drop:
                            filldict[attr.name] = val
                    else:
                        filldict[attr.name] = {}
                        self.validate(request, attr, filldict[attr.name],
                                      key + '.')
            except colander.Invalid as exc:
                filldict[attr.name] = None
                for key, val in exc.asdict().items():
                    request.yards.errors[prefix + key] = val

    def __call__(self, request):
        self.validate(request, self.schema, request.yards._data)
        if request.yards.errors:
            raise ValidationFailure(request.yards.errors)
        return request


class RequestSchemaPredicate(RequestSchema):
    check_csrf_token = None  # default value in the includeme

    def __init__(self, schema, config):
        self._check_csrf = not getattr(schema, 'DISABLE_CSRF_CHECK',
                                       not self.check_csrf_token)
        super(RequestSchemaPredicate, self).__init__(schema)

    def text(self):
        return 'request-schema = %s' % (self.schema,)

    phash = text

    def __call__(self, context, request):
        if request.method not in ('POST', 'PUT', 'PATCH', 'DELETE'):
            return True
        try:
            super(RequestSchemaPredicate, self).__call__(request)
        except ValidationFailure:
            # Using predicated, validation errors ared delayed
            # in the view
            pass

        if self._check_csrf and not check_csrf(request, raises=False):
            log.warn('CSRF Attack from {0}'.format(request.client_addr))
            log.info(request.locale_name)

            message = _("Invalid value")
            log.info(request.locale_name)
            if request.localizer:
                message = request.localizer.translate(message,
                                                      domain='pyramid-yards')
            request.yards.errors['csrf_token'] = message

        # Always return True, otherwise pyramid will raise an
        # http error, and we don't want that.
        return True
