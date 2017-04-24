from __future__ import absolute_import, unicode_literals

from django.utils.encoding import force_text
from django.utils.functional import cached_property

from wagtail.wagtailcore.blocks import RichTextBlock

from wagtaildraftail.draft_text import DraftText
from wagtaildraftail.forms import SerializedJSONField


class DraftailTextBlock(RichTextBlock):
    """
    StreamField block to render a rich text editor powered by Draftail.
    """
    def __init__(self, required=True, help_text=None, editor='default_draftail', **kwargs):
        super(DraftailTextBlock, self).__init__(required, help_text, editor, **kwargs)

    def get_default(self):
        if isinstance(self.meta.default, DraftText):
            return self.meta.default
        else:
            return DraftText(self.meta.default)

    @cached_property
    def field(self):
        from wagtail.wagtailadmin.rich_text import get_rich_text_editor_widget
        return SerializedJSONField(widget=get_rich_text_editor_widget(self.editor), **self.field_options)

    def to_python(self, value):
        return DraftText(value)

    def value_from_form(self, value):
        return DraftText(value)

    def get_searchable_content(self, value):
        if not isinstance(value, DraftText):
            value = DraftText(value)
        return [force_text(value.__html__())]

    class Meta:
        icon = "doc-full"
        default = '{}'
