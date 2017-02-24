from __future__ import absolute_import, unicode_literals

import json

from django.utils.encoding import force_text
from django.utils.functional import cached_property
from wagtail.wagtailcore.blocks import FieldBlock

import forms
from filters import draft_text


class DraftailTextBlock(FieldBlock):
    """
    StreamField block to render a rich text editor powered by Draftail.
    """
    def __init__(self, required=True, help_text=None, editor='default_draftjs', **kwargs):
        self.field_options = {'required': required, 'help_text': help_text}
        self.editor = editor
        super(DraftailTextBlock, self).__init__(**kwargs)

    def get_default(self):
        return self.meta.default

    def to_python(self, value):
        return value

    def get_prep_value(self, value):
        return value

    @cached_property
    def field(self):
        from wagtail.wagtailadmin.rich_text import get_rich_text_editor_widget
        return forms.SerializedJSONField(widget=get_rich_text_editor_widget(self.editor), **self.field_options)

    def value_for_form(self, value):
        try:
            return value
        except:
            return {}

    def value_from_form(self, value):
        """
        Ensure we have a serialisable JSON object.
        """
        if value:
            try:
                return json.dumps(json.loads(value))
            except:
                return None
        return None

    def get_searchable_content(self, value):
        return [force_text(value)]

    def render_basic(self, value, context=None):
        """
        Return a text rendering of 'value', suitable for display on templates. render() will fall back on
        this if the block does not define a 'template' property.
        """

        return draft_text(value, render=True) if value else ''

    class Meta:
        icon = "doc-full"
        default = '{}'
