from __future__ import absolute_import, unicode_literals

import validators
from django import forms


class SerializedJSONField(forms.CharField):
    empty_values = list(validators.EMPTY_SERIALIZED_JSON_VALUES)
