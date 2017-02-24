from __future__ import absolute_import, unicode_literals

import json

from django import template
from django.utils.safestring import mark_safe
from draftjs_exporter.html import HTML

from wagtaildraftail.settings import get_exporter_config


register = template.Library()


class DraftValue:
    def __init__(self, data):
        self.data = data
        self.exporter = HTML(get_exporter_config())

    def __html__(self):
        return self.exporter.render(self.data)


@register.filter
def draft_text(text):
    data = json.loads(text)
    node = DraftValue(data)

    return mark_safe(node.__html__())
