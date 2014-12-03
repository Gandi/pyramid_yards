import logging
import colander

log = logging.getLogger(__name__)


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

    def __getitem__(self, key):
        return self._data[key]

    def __contains__(self, key):
        return key in self._data

    def get(self, key, default=None):
        return self._data.get(key, default)


class RequestSchemaPredicate(object):
    def __init__(self, schema, config):
        self.schema = schema

    def text(self):
        return 'request-schema = %s' % (self.schema,)

    phash = text

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
                    filldict[attr.name] = {}
                    self.validate(request, attr, filldict[attr.name],
                                  key + '.')
            except colander.Invalid as exc:
                for key, val in exc.asdict().items():
                    request.yards.errors[prefix + key] = val

    def __call__(self, context, request):
        if request.method not in ('POST', 'PUT'):
            return True
        self.validate(request, self.schema, request.yards._data)
        # Always return True, otherwise pyramid will raise an
        # http error, and we don't want that.
        return True
