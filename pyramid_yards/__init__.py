"""
pyramid_kvs is a Key/Value Store helpers for pyramid.

See the README.rst file for more information.
"""

__version__ = '0.4'

from pyramid.events import NewRequest

from .yards import Yards, RequestSchemaPredicate


def subscribe_yards(event):
    request = event.request
    request.set_property(Yards(request), 'yards', reify=True)


def includeme(config):
    config.add_subscriber(subscribe_yards, NewRequest)
    config.add_view_predicate('request_schema', RequestSchemaPredicate)
