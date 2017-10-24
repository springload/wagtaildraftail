from __future__ import absolute_import, unicode_literals

import json
import re

from bs4 import BeautifulSoup
from django.test import SimpleTestCase
from draftjs_exporter.constants import BLOCK_TYPES, ENTITY_TYPES

from wagtaildraftail.widgets import DraftailTextArea


CUSTOM_OPTIONS = {
    'entityTypes': [
        {
            'label': 'Link',
            'type': ENTITY_TYPES.LINK,
            'icon': 'icon-link',
            'source': 'LinkSource',
            'decorator': 'Link',
        }
    ],
    'blockTypes': [
        {'label': 'H1', 'type': BLOCK_TYPES.HEADER_ONE},
        {'label': 'H2', 'type': BLOCK_TYPES.HEADER_TWO},
        {'label': 'H3', 'type': BLOCK_TYPES.HEADER_THREE},
    ],
}


class DraftailTextAreaWidgetTestCase(SimpleTestCase):
    def extract_options_from_script(self, script):
        match = re.match(
            r'window\.wagtailDraftail\.initEditor\(\'default_editor\', (\{.*\})\)$',
            script
        )
        self.assertTrue(match, "Call to initEditor not found in: %r" % script)
        return json.loads(match.group(1))

    def test_rendering_with_explicit_options(self):
        """
        If a widget is initialised with a (populated) options dict but no
        features list, the options dict should be passed on to the JS
        """

        widget = DraftailTextArea(options=CUSTOM_OPTIONS)

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

        options = self.extract_options_from_script(soup.script.text)
        self.assertDictEqual(options, CUSTOM_OPTIONS)

    def test_rendering_with_default_features(self):
        """
        When no options or features are specified for the widget,
        the default feature set should be used
        """

        widget = DraftailTextArea()

        html = widget.render('default_editor', json.dumps({'key': 'val'}), {'id': 'id'})
        soup = BeautifulSoup(html, 'html.parser')

        self.assertIsNotNone(soup.input)
        self.assertIsNotNone(soup.script)

        self.assertDictContainsSubset({
            'type': 'hidden',
            'name': 'default_editor',
            'value': '{"key": "val"}',
            'id': 'id'
        }, soup.input.attrs)

        options = self.extract_options_from_script(soup.script.text)
        self.assertTrue(options['enableHorizontalRule'])
        # default features include H3 but not H1
        self.assertFalse([block for block in options['blockTypes'] if block['type'] == BLOCK_TYPES.HEADER_ONE])
        self.assertTrue([block for block in options['blockTypes'] if block['type'] == BLOCK_TYPES.HEADER_THREE])

        self.assertTrue([entity for entity in options['entityTypes'] if entity['type'] == ENTITY_TYPES.LINK])
        self.assertTrue([entity for entity in options['entityTypes'] if entity['type'] == ENTITY_TYPES.IMAGE])

    def test_rendering_with_explicit_features(self):
        """
        A features list passed to the widget should generate an options dict for those
        features (overriding any options dict that was passed)
        """

        widget = DraftailTextArea(options=CUSTOM_OPTIONS, features=['h1', 'image'])

        html = widget.render('default_editor', json.dumps({'key': 'val'}), {'id': 'id'})
        soup = BeautifulSoup(html, 'html.parser')

        self.assertIsNotNone(soup.input)
        self.assertIsNotNone(soup.script)

        self.assertDictContainsSubset({
            'type': 'hidden',
            'name': 'default_editor',
            'value': '{"key": "val"}',
            'id': 'id'
        }, soup.input.attrs)

        options = self.extract_options_from_script(soup.script.text)
        self.assertFalse('enableHorizontalRule' in options)
        self.assertTrue([block for block in options['blockTypes'] if block['type'] == BLOCK_TYPES.HEADER_ONE])
        self.assertFalse([block for block in options['blockTypes'] if block['type'] == BLOCK_TYPES.HEADER_THREE])

        self.assertFalse([entity for entity in options['entityTypes'] if entity['type'] == ENTITY_TYPES.LINK])
        self.assertTrue([entity for entity in options['entityTypes'] if entity['type'] == ENTITY_TYPES.IMAGE])

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
