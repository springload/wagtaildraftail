from __future__ import absolute_import, unicode_literals

import json
import unittest

from bs4 import BeautifulSoup

from wagtaildraftail.widgets import DraftailTextArea


class DraftailTextAreaWidgetTestCase(unittest.TestCase):
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
