from __future__ import absolute_import, unicode_literals

import unittest

from django.core.exceptions import ValidationError

from wagtaildraftail import forms


class SerializedJSONFieldTestCase(unittest.TestCase):

    def setUp(self):
        self.field = forms.SerializedJSONField(required=True)

    def test_none_is_empty_value(self):
        with self.assertRaises(ValidationError):
            self.field.clean(None)

    def test_empty_string_is_empty_value(self):
        with self.assertRaises(ValidationError):
            self.field.clean('')

    def test_serialized_empty_list_is_empty_value(self):
        with self.assertRaises(ValidationError):
            self.field.clean('[]')

    def test_serialized_empty_dict_is_empty_value(self):
        with self.assertRaises(ValidationError):
            self.field.clean('{}')
