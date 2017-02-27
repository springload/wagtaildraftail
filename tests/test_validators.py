from __future__ import absolute_import, unicode_literals

import unittest

from wagtaildraftail.validators import EMPTY_SERIALIZED_JSON_VALUES


class TestValidators(unittest.TestCase):
    def test_empty_serialised(self):
        self.assertIsInstance(EMPTY_SERIALIZED_JSON_VALUES, tuple)
