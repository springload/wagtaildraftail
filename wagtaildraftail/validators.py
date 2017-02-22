from __future__ import absolute_import, unicode_literals

# `None` and empty string aren't valid JSON but it's safer to include them as potential empty values.
EMPTY_SERIALIZED_JSON_VALUES = (None, '', '[]', '{}')
