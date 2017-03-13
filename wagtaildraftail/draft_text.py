from __future__ import absolute_import, unicode_literals

import json

from draftjs_exporter.html import HTML

from wagtail.wagtailcore.rich_text import RichText
from wagtaildraftail.settings import get_exporter_config


class DraftText(RichText):
    def __init__(self, value, **kwargs):
        super(DraftText, self).__init__(value or '{}', **kwargs)
        self.exporter = HTML(get_exporter_config())

    def get_json(self):
        return self.source

    def __html__(self):
        return self.exporter.render(json.loads(self.source))
