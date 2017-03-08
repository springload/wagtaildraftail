from __future__ import absolute_import, unicode_literals

import unittest


class TestWagtailBlocks(unittest.TestCase):
    def test_regression_absolute_import(self):
        from wagtaildraftail.blocks import DraftailTextBlock  # noqa

        # try:
        #     from wagtaildraftail.blocks import DraftailTextBlock  # noqa
        # except Exception:
        #     self.fail("Import of the DraftailTextBlock should not raise exceptions")
