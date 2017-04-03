from __future__ import absolute_import, unicode_literals

import unittest

from django.test import override_settings

from wagtaildraftail import blocks, draft_text, forms, widgets


class DraftailTextBlockTestCase(unittest.TestCase):

    def test_get_default_with_string_default(self):
        class StringDefaultDraftailTextBlock(blocks.DraftailTextBlock):
            class Meta:
                default = '{}'

        block = StringDefaultDraftailTextBlock()
        default = block.get_default()
        expected_default = draft_text.DraftText('{}')

        self.assertIsInstance(default, draft_text.DraftText)
        self.assertEqual(default, expected_default)

    def test_get_default_with_node_default(self):
        class NodeDefaultDraftailTextBlock(blocks.DraftailTextBlock):
            class Meta:
                default = draft_text.DraftText('{}')

        block = NodeDefaultDraftailTextBlock()
        default = block.get_default()
        expected_default = draft_text.DraftText('{}')

        self.assertIsInstance(default, draft_text.DraftText)
        self.assertEqual(default, expected_default)

    def test_field_class(self):
        block = blocks.DraftailTextBlock()

        self.assertIsInstance(block.field, forms.SerializedJSONField)

    @override_settings(WAGTAILADMIN_RICH_TEXT_EDITORS={
        'test_editor': {
            'WIDGET': 'wagtaildraftail.widgets.DraftailTextArea',
        }
    })
    def test_field_is_initialized_with_widget(self):
        block = blocks.DraftailTextBlock(editor='test_editor')

        self.assertIsInstance(block.field.widget, widgets.DraftailTextArea)

    def test_field_is_initialized_with_options(self):
        options = {'required': False, 'help_text': 'weee'}
        block = blocks.DraftailTextBlock(**options)

        self.assertEqual(block.field.required, options['required'])
        self.assertEqual(block.field.help_text, options['help_text'])

    def test_to_python(self):
        value = '{"entityMap": {}, "blocks": [{"entityRanges": [], "inlineStyleRanges": [{"style": "BOLD", "length": 7, "offset": 0}], "type": "unstyled", "text": "Cupcake ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...", "depth": 0, "key": "en564", "data": {}}]}'  # noqa: E501
        python_value = blocks.DraftailTextBlock().to_python(value)
        expected_python_value = draft_text.DraftText(value)

        self.assertIsInstance(python_value, draft_text.DraftText)
        self.assertEqual(python_value, expected_python_value)

    def test_value_from_form(self):
        value = '{"entityMap": {}, "blocks": [{"entityRanges": [], "inlineStyleRanges": [{"style": "BOLD", "length": 7, "offset": 0}], "type": "unstyled", "text": "Cupcake ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...", "depth": 0, "key": "en564", "data": {}}]}'  # noqa: E501
        form_value = blocks.DraftailTextBlock().value_from_form(value)
        expected_form_value = draft_text.DraftText(value)

        self.assertIsInstance(form_value, draft_text.DraftText)
        self.assertEqual(form_value, expected_form_value)

    def test_get_searchable_content_with_string_value(self):
        value = '{"entityMap": {}, "blocks": [{"entityRanges": [], "inlineStyleRanges": [{"style": "BOLD", "length": 7, "offset": 0}], "type": "unstyled", "text": "Cupcake ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...", "depth": 0, "key": "en564", "data": {}}]}'  # noqa: E501
        searchable_content = blocks.DraftailTextBlock().get_searchable_content(value)
        expected_searchable_content = [
            '<p><strong>Cupcake</strong> ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...</p>']

        self.assertEqual(searchable_content, expected_searchable_content)

    def test_get_searchable_content_with_node_value(self):
        value = draft_text.DraftText('{"entityMap": {}, "blocks": [{"entityRanges": [], "inlineStyleRanges": [{"style": "BOLD", "length": 7, "offset": 0}], "type": "unstyled", "text": "Cupcake ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...", "depth": 0, "key": "en564", "data": {}}]}')  # noqa: E501
        searchable_content = blocks.DraftailTextBlock().get_searchable_content(value)
        expected_searchable_content = [
            '<p><strong>Cupcake</strong> ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...</p>']

        self.assertEqual(searchable_content, expected_searchable_content)
