from __future__ import absolute_import, unicode_literals

import json

from draftjs_exporter.html import HTML

from jinja2 import Markup

from .settings import get_exporter_config


class DraftValue:
    def __init__(self, data):
        self.data = data
        self.exporter = HTML(get_exporter_config())

    def __html__(self):
        return Markup(self.exporter.render(self.data))


def draft_text(text, render=False):
    """
    Draft.js equivalent of the |richtext filter.

    :type text: str
    :param text:
    :type render: boolean
    :param render: whether to render automatically or return a template node; default to false, i.e. return a node
    """

    data = json.loads(text)
    node = DraftValue(data)

    return node.__html__() if render else node
