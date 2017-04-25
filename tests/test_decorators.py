from __future__ import absolute_import, unicode_literals

import unittest

from draftjs_exporter.constants import BLOCK_TYPES
from draftjs_exporter.dom import DOM
from wagtail.wagtailcore.models import Page, Site

from home.models import HomePage
from wagtaildraftail.decorators import BR, HR, MISSING_RESOURCE_URL, Icon, Link


class TestIcon(unittest.TestCase):
    def test_render(self):
        output = DOM.render(DOM.create_element(Icon, {'name': 'rocket'}))
        expected_output = '<svg class="icon"><use xlink:href="#icon-rocket"></use></svg>'
        self.assertEqual(output, expected_output)


class TestHR(unittest.TestCase):
    def test_render(self):
        self.assertEqual(DOM.render(DOM.create_element(HR)), '<hr/>')


class TestBR(unittest.TestCase):
    def test_render(self):
        element = DOM.create_element(BR, {'block': {'type': BLOCK_TYPES.UNSTYLED}}, '\n')
        self.assertEqual(DOM.render(element), '<br/>')

    def test_render_code_block(self):
        element = DOM.create_element(BR, {'block': {'type': BLOCK_TYPES.CODE}}, '\n')
        self.assertEqual(element, '\n')


class TestLink(unittest.TestCase):
    """Tests several scenarios regarding rendering of a link."""

    def setUp(self):
        """Test."""
        root_site = Site.objects.get(is_default_site=True)
        root_page = Page.objects.get(id=root_site.root_page_id)
        page = HomePage(title="Testpage")
        root_page.add_child(instance=page)
        self.page = page

    def test_internal_link(self):
        """Test if the page URL is set."""
        input_props = {
            'linkType': 'page',
            'id': self.page.pk
        }
        output = DOM.render(DOM.create_element(Link, input_props))
        self.assertEqual(output, '<a href="{0}"></a>'.format(self.page.url))

    def test_internal_link_href_fallback(self):
        """Test if the fallback href is used when the page does not exist."""
        input_props = {
            'linkType': 'page',
            'id': 999,
        }
        output = DOM.render(DOM.create_element(Link, input_props))
        self.assertEqual(output, '<a href="{0}"></a>'.format(MISSING_RESOURCE_URL))

    def test_external_link(self):
        """Test if external links are passed as such."""
        input_props = {
            'linkType': 'external',
            'url': 'http://test.test',
        }
        output = DOM.render(DOM.create_element(Link, input_props))
        self.assertEqual(output, '<a href="http://test.test"></a>')

    def test_with_title(self):
        """Test if title attribute is set."""
        input_props = {
            'linkType': 'external',
            'url': 'http://test.test',
            'title': 'Test title'
        }
        output = DOM.render(DOM.create_element(Link, input_props))
        self.assertEqual(output, '<a href="http://test.test" title="Test title"></a>')

    def test_with_children(self):
        """Test if child content is rendered."""
        input_props = {
            'linkType': 'page',
            'id': self.page.pk,
        }
        output = DOM.render(DOM.create_element(Link, input_props, 'anchor content'))
        self.assertEqual(output, '<a href="{0}">anchor content</a>'.format(self.page.url))
