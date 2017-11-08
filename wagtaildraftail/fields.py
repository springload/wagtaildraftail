from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import force_text

from wagtail import VERSION as WAGTAIL_VERSION

from .draft_text import DraftText
from .validators import EMPTY_SERIALIZED_JSON_VALUES


class DraftailTextField(models.TextField):
    empty_values = list(EMPTY_SERIALIZED_JSON_VALUES)

    def __init__(self, *args, **kwargs):
        self.editor = kwargs.pop('editor', 'default_draftail')
        self.features = kwargs.pop('features', None)
        super(DraftailTextField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from wagtail.wagtailadmin.rich_text import get_rich_text_editor_widget
        if WAGTAIL_VERSION >= (1, 12):
            defaults = {'widget': get_rich_text_editor_widget(self.editor, features=self.features)}
        else:
            defaults = {'widget': get_rich_text_editor_widget(self.editor)}
        defaults.update(kwargs)
        return super(DraftailTextField, self).formfield(**defaults)

    def to_python(self, value):
        if not isinstance(value, DraftText):
            value = DraftText(value)
        return value

    def get_prep_value(self, value):
        if isinstance(value, DraftText):
            value = value.get_json()

        value = super(DraftailTextField, self).get_prep_value(value)

        # Django>1.8 does `to_python` in get_prep_value
        if isinstance(value, DraftText):
            value = value.get_json()

        return value

    def from_db_value(self, value, *args, **kwargs):
        if not isinstance(value, DraftText):
            value = DraftText(value)
        return value

    def value_to_string(self, obj):
        if obj is not None:
            value = self.value_from_object(obj)
        else:
            value = self.get_default()

        if isinstance(value, DraftText):
            value = value.get_json()

        return value

    def get_searchable_content(self, value):
        if not isinstance(value, DraftText):
            value = DraftText(value)
        return [force_text(value.__html__())]
