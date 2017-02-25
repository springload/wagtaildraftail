from __future__ import absolute_import, unicode_literals

from django.test import TestCase

from draftjs_exporter.dom import DOM
from wagtaildraftail.decorators import HR, Icon


class TestIcon(TestCase):
    def test_render(self):
        self.assertEqual(DOM.render(DOM.create_element(Icon, {'name': 'rocket'})), '<svg class="icon"><use xlink:href="#icon-rocket"></use></svg>')
