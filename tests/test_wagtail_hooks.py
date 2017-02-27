from __future__ import absolute_import, unicode_literals

import unittest

from wagtaildraftail.wagtail_hooks import draftail_editor_css, draftail_editor_js


class TestWagtailHooks(unittest.TestCase):
    def test_editor_css(self):
        self.assertEqual(draftail_editor_css(), '<link rel="stylesheet" href="/static/wagtaildraftail/wagtaildraftail.css">')

    def test_editor_js(self):
        self.assertEqual(draftail_editor_js(), '<script src="/static/wagtaildraftail/wagtaildraftail.js"></script>')
