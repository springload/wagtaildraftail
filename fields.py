from django.db import models

from wagtailaddons.drafteditor import validators


class DraftailTextField(models.TextField):
    empty_values = list(validators.EMPTY_SERIALIZED_JSON_VALUES)

    def __init__(self, *args, **kwargs):
        self.editor = kwargs.pop('editor', 'default_draftjs')
        super(DraftailTextField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        from wagtail.wagtailadmin.rich_text import get_rich_text_editor_widget
        defaults = {'widget': get_rich_text_editor_widget(self.editor)}
        defaults.update(kwargs)
        return super(DraftailTextField, self).formfield(**defaults)
