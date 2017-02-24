from __future__ import absolute_import, unicode_literals

from django import forms

from .validators import EMPTY_SERIALIZED_JSON_VALUES


class SerializedJSONField(forms.CharField):
    empty_values = list(EMPTY_SERIALIZED_JSON_VALUES)
