from django.utils.html import format_html
from django.contrib.staticfiles.templatetags.staticfiles import static
from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_js')
def draftail_editor_js():
    return format_html('<script src="{0}"></script>',
                       static('wagtaildraftail/wagtaildraftail.bundle.js'))
