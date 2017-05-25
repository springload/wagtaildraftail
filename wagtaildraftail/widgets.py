from __future__ import absolute_import, unicode_literals

import json
import logging

from django import forms
from django.utils.inspect import func_supports_parameter

from draftjs_exporter.constants import ENTITY_TYPES

from wagtail.utils.widgets import WidgetWithScript
from wagtail.wagtailimages.formats import get_image_formats

from .draft_text import DraftText


def get_all_image_formats():
    return [{'label': str(f.label), 'value': f.name} for f in get_image_formats()]


class DraftailTextArea(WidgetWithScript, forms.HiddenInput):
    """
    Field widget to render a rich text editor powered by Draftail.
    """
    def __init__(self, attrs=None, options=None):
        self.options = self.intercept_image_formats(options or {})

        super(DraftailTextArea, self).__init__(attrs)

    def intercept_image_formats(self, options):
        """
        Load all image formats if needed.
        """
        if 'entityTypes' in options:
            for entity in options['entityTypes']:
                if entity['type'] == ENTITY_TYPES.IMAGE and 'imageFormats' in entity:
                    if entity['imageFormats'] == '__all__':
                        entity['imageFormats'] = get_all_image_formats()

        return options

    def render(self, name, value=None, attrs=None, renderer=None):
        json_value = value

        if json_value is None or json_value is '':
            value = None
        else:
            if isinstance(json_value, DraftText):
                json_value = json_value.get_json()
            try:
                value = json.loads(json_value)
            except (ValueError, TypeError):
                value = {}
                logging.getLogger(__name__).warn('Cannot handle {} as JSON'.format(json_value))

        encoded_value = json.dumps(value)

        parent = super(DraftailTextArea, self)

        if func_supports_parameter(parent.render, 'renderer'):  # >= Django 1.11
            return parent.render(name, encoded_value, attrs, renderer)
        else:
            return parent.render(name, encoded_value, attrs)

    def render_js_init(self, id_, name, value):
        return "window.wagtailDraftail.initEditor('{name}', {opts})".format(
            name=name, opts=json.dumps(self.options))

    def value_from_datadict(self, data, files, name):
        json_value = super(DraftailTextArea, self).value_from_datadict(data, files, name)

        if json_value is None:
            return None
        elif json_value is '':
            value = {}
        else:
            if isinstance(json_value, DraftText):
                json_value = json_value.get_json()
            try:
                value = json.loads(json_value)
            except (ValueError, TypeError):
                value = {}
                logging.getLogger(__name__).warning('Cannot handle {} as JSON'.format(json_value))

        return json.dumps(value)
