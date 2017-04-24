from __future__ import absolute_import, unicode_literals

import json

from bs4 import BeautifulSoup
from django import template

register = template.Library()


@register.filter
def pretty_json(data):
    if isinstance(data, str):
        data = json.loads(data)

    return json.dumps(data, indent=4)


@register.filter
def pretty_html(data):
    soup = BeautifulSoup(data, 'html5lib')
    body = soup.find('body')
    return body.prettify()  # TODO: Strip the body tag.
