from __future__ import absolute_import, unicode_literals

import json
import unittest

from wagtaildraftail.widgets import DraftailTextArea


class DraftailTextAreaWidgetTestCase(unittest.TestCase):
    def test_rendering(self):
        widget = DraftailTextArea()

        html = widget.render('default_editor', json.dumps({'key': 'val'}), {'id': 'id'})

        self.assertEqual(html, (
            r'''<input type="hidden" name="default_editor" '''
            r'''value="{&quot;key&quot;: &quot;val&quot;}" '''
            r'''id="id" /><script>window.wagtailDraftail.initEditor('default_editor', {})</script>'''))
