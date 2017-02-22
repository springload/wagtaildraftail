from __future__ import absolute_import, unicode_literals

from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html
from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_js')
def draftail_editor_js():
    return format_html('<script src="{0}"></script>', static('wagtaildraftail/wagtaildraftail.js'))


@hooks.register('insert_editor_css')
def draftail_editor_css():
    return format_html('<link rel="stylesheet" href="{0}">', static('wagtaildraftail/wagtaildraftail.css'))
