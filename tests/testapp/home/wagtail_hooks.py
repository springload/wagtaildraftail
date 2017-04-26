from __future__ import absolute_import, unicode_literals

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_js')
def button_entity_js():
    return format_html(
        '<script src="{}"></script>',
        static('button_entity.js')
    )


@hooks.register('insert_editor_css')
def button_entity_css():
    return format_html(
        '<link rel="stylesheet" href="{}">',
        static('button_entity.css')
    )
