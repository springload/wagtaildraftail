from __future__ import absolute_import, unicode_literals

from django.db import models

from .validators import EMPTY_SERIALIZED_JSON_VALUES


class DraftailTextField(models.TextField):
    empty_values = list(EMPTY_SERIALIZED_JSON_VALUES)

    def __init__(self, *args, **kwargs):
        self.editor = kwargs.pop('editor', 'default_draftjs')
        super(DraftailTextField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from wagtail.wagtailadmin.rich_text import get_rich_text_editor_widget
        defaults = {'widget': get_rich_text_editor_widget(self.editor)}
        defaults.update(kwargs)
        return super(DraftailTextField, self).formfield(**defaults)
