from draftjs_exporter.dom import DOM
from wagtail.wagtailcore.models import Page

MISSING_RESOURCE_CLASS = 'button--missing-resource'
MISSING_RESOURCE_URL = '#'


class Button:
    def render(self, props):
        link_type = props.get('linkType', '')

        if link_type == 'page':
            try:
                page_id = props.get('id')
                page = Page.objects.get(id=page_id)
                href = page.url
            except Page.DoesNotExist:
                href = props.get('url', MISSING_RESOURCE_URL)
        else:
            href = props.get('url', MISSING_RESOURCE_URL)

        anchor_properties = {
            'className': 'button',
            'onclick': "window.location.href='{}'".format(href),
        }

        return DOM.create_element('button', anchor_properties, props['children'])
