from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.constants import BLOCK_TYPES
from draftjs_exporter.dom import DOM
from wagtaildraftail.decorators import BR, HR, Icon


class TestIcon(unittest.TestCase):
    def test_render(self):
        self.assertEqual(DOM.render(DOM.create_element(Icon, {'name': 'rocket'})), '<svg class="icon"><use xlink:href="#icon-rocket"></use></svg>')


class TestHR(unittest.TestCase):
    def test_render(self):
        self.assertEqual(DOM.render(DOM.create_element(HR)), '<hr/>')


class TestBR(unittest.TestCase):
    def test_render(self):
        self.assertEqual(DOM.render(DOM.create_element(BR, {
            'block_type': BLOCK_TYPES.UNSTYLED,
            'children': '\n',
        })), '<br/>')

    def test_render_code_block(self):
        self.assertEqual(DOM.create_element(BR, {
            'block_type': BLOCK_TYPES.CODE,
            'children': '\n',
        }), '\n')
