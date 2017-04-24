from __future__ import absolute_import, unicode_literals

import unittest

from wagtail.wagtailcore.hooks import get_hooks

from wagtaildraftail.wagtail_hooks import draftail_editor_css, draftail_editor_js


class TestWagtailHooks(unittest.TestCase):
    def test_editor_css(self):
        self.assertEqual(
            draftail_editor_css(), '<link rel="stylesheet" href="/static/wagtaildraftail/wagtaildraftail.css">')

    def test_insert_editor_css_hook(self):
        hooks = get_hooks('insert_editor_css')
        self.assertIn(draftail_editor_css, hooks, 'Editor CSS should be inserted automatically.')

    def test_editor_js(self):
        self.assertEqual(
            draftail_editor_js(), '<script src="/static/wagtaildraftail/wagtaildraftail.js"></script>')

    def test_insert_editor_js(self):
        hooks = get_hooks('insert_editor_js')
        self.assertIn(draftail_editor_js, hooks, 'Editor JS should be inserted automatically.')
