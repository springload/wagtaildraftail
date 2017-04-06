from __future__ import absolute_import, unicode_literals

import unittest

from django.forms import widgets as djwidgets
from django.test import override_settings

from wagtaildraftail import draft_text, fields, widgets


class DraftailTextFieldTestCase(unittest.TestCase):

    def test_init_has_default_editor(self):
        field = fields.DraftailTextField()

        self.assertEqual(field.editor, 'default_draftail')

    def test_init_with_custom_editor(self):
        editor = 'custom_editor'
        field = fields.DraftailTextField(editor=editor)

        self.assertEqual(field.editor, editor)

    @override_settings(WAGTAILADMIN_RICH_TEXT_EDITORS={
        'test_editor': {
            'WIDGET': 'wagtaildraftail.widgets.DraftailTextArea',
        }
    })
    def test_formfield_is_initialized_with_widget(self):
        field = fields.DraftailTextField(editor='test_editor')
        formfield = field.formfield()

        self.assertIsInstance(formfield.widget, widgets.DraftailTextArea)

    def test_formfield_can_overwrite_widget(self):
        field = fields.DraftailTextField()
        formfield = field.formfield(widget=djwidgets.Textarea)

        self.assertIsInstance(formfield.widget, djwidgets.Textarea)

    def test_to_python_with_string_value(self):
        value = '{"entityMap": {}, "blocks": [{"entityRanges": [], "inlineStyleRanges": [{"style": "BOLD", "length": 7, "offset": 0}], "type": "unstyled", "text": "Cupcake ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...", "depth": 0, "key": "en564", "data": {}}]}'  # noqa: E501
        python_value = fields.DraftailTextField().to_python(value)
        expected_python_value = draft_text.DraftText(value)

        self.assertIsInstance(python_value, draft_text.DraftText)
        self.assertEqual(python_value, expected_python_value)

    def test_to_python_with_node_value(self):
        value = '{"entityMap": {}, "blocks": [{"entityRanges": [], "inlineStyleRanges": [{"style": "BOLD", "length": 7, "offset": 0}], "type": "unstyled", "text": "Cupcake ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...", "depth": 0, "key": "en564", "data": {}}]}'  # noqa: E501
        python_value = fields.DraftailTextField().to_python(draft_text.DraftText(value))
        expected_python_value = draft_text.DraftText(value)

        self.assertIsInstance(python_value, draft_text.DraftText)
        self.assertEqual(python_value, expected_python_value)

    def test_get_prep_value_with_string_value(self):
        value = '{"entityMap": {}, "blocks": [{"entityRanges": [], "inlineStyleRanges": [{"style": "BOLD", "length": 7, "offset": 0}], "type": "unstyled", "text": "Cupcake ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...", "depth": 0, "key": "en564", "data": {}}]}'  # noqa: E501
        prep_value = fields.DraftailTextField().get_prep_value(value)

        self.assertEqual(prep_value, value)

    def test_get_prep_value_with_node_value(self):
        value = '{"entityMap": {}, "blocks": [{"entityRanges": [], "inlineStyleRanges": [{"style": "BOLD", "length": 7, "offset": 0}], "type": "unstyled", "text": "Cupcake ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...", "depth": 0, "key": "en564", "data": {}}]}'  # noqa: E501
        prep_value = fields.DraftailTextField().get_prep_value(draft_text.DraftText(value))

        self.assertEqual(prep_value, value)

    def test_from_db_value(self):
        value = '{"entityMap": {}, "blocks": [{"entityRanges": [], "inlineStyleRanges": [{"style": "BOLD", "length": 7, "offset": 0}], "type": "unstyled", "text": "Cupcake ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...", "depth": 0, "key": "en564", "data": {}}]}'  # noqa: E501
        from_db_value = fields.DraftailTextField().from_db_value(value)
        expected_from_db_value = draft_text.DraftText(value)

        self.assertIsInstance(from_db_value, draft_text.DraftText)
        self.assertEqual(from_db_value, expected_from_db_value)

    def test_value_to_string_with_none_value(self):
        pass  # TODO

    def test_value_to_string_with_obj_value(self):
        pass  # TODO

    def test_get_searchable_content_with_string_value(self):
        value = '{"entityMap": {}, "blocks": [{"entityRanges": [], "inlineStyleRanges": [{"style": "BOLD", "length": 7, "offset": 0}], "type": "unstyled", "text": "Cupcake ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...", "depth": 0, "key": "en564", "data": {}}]}'  # noqa: E501
        searchable_content = fields.DraftailTextField().get_searchable_content(value)
        expected_searchable_content = [
            '<p><strong>Cupcake</strong> ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...</p>']

        self.assertEqual(searchable_content, expected_searchable_content)

    def test_get_searchable_content_with_node_value(self):
        value = draft_text.DraftText('{"entityMap": {}, "blocks": [{"entityRanges": [], "inlineStyleRanges": [{"style": "BOLD", "length": 7, "offset": 0}], "type": "unstyled", "text": "Cupcake ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...", "depth": 0, "key": "en564", "data": {}}]}')  # noqa: E501
        searchable_content = fields.DraftailTextField().get_searchable_content(value)
        expected_searchable_content = [
            '<p><strong>Cupcake</strong> ipsum dolor sit amet muffin drag\u00e9e cupcake biscuit...</p>']

        self.assertEqual(searchable_content, expected_searchable_content)
