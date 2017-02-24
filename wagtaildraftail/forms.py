from __future__ import absolute_import, unicode_literals

from .validators import EMPTY_SERIALIZED_JSON_VALUES
from django import forms


class SerializedJSONField(forms.CharField):
    empty_values = list(EMPTY_SERIALIZED_JSON_VALUES)
