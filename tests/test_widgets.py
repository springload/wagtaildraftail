from __future__ import absolute_import, unicode_literals

import json

from bs4 import BeautifulSoup
from django.test import SimpleTestCase

from wagtaildraftail.widgets import DraftailTextArea


class DraftailTextAreaWidgetTestCase(SimpleTestCase):
    def test_rendering(self):
        widget = DraftailTextArea()

        html = widget.render('default_editor', json.dumps({'key': 'val'}), {'id': 'id'})

        # <input type="hidden"
        #        name="default_editor"
        #        value="{&quot;key&quot;: &quot;val&quot;}"
        #        id="id" />
        # <script>window.wagtailDraftail.initEditor('default_editor', {})</script>

        soup = BeautifulSoup(html, 'html.parser')

        self.assertIsNotNone(soup.input)
        self.assertIsNotNone(soup.script)

        self.assertDictContainsSubset({
            'type': 'hidden',
            'name': 'default_editor',
            'value': '{"key": "val"}',
            'id': 'id'
        }, soup.input.attrs)

        self.assertEquals(soup.script.text, r"window.wagtailDraftail.initEditor('default_editor', {})")

    def test_media(self):
        widget = DraftailTextArea()
        media_html = widget.media.__html__()

        self.assertInHTML(
            '<link href="/static/wagtaildraftail/wagtaildraftail.css" type="text/css" media="all" rel="stylesheet" />',
            media_html
        )
        self.assertInHTML(
            '<script type="text/javascript" src="/static/wagtaildraftail/wagtaildraftail.js"></script>',
            media_html
        )
