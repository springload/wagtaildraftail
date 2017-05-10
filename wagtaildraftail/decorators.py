from __future__ import absolute_import, unicode_literals

import re

from draftjs_exporter.constants import BLOCK_TYPES
from draftjs_exporter.dom import DOM
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.models import get_document_model
from wagtail.wagtailembeds.format import embed_to_frontend_html
from wagtail.wagtailimages.formats import get_image_format
from wagtail.wagtailimages.shortcuts import get_rendition_or_not_found

from .utils import get_document_meta

try:
    from wagtail.wagtailimages import get_image_model
except ImportError:  # Fallback to Wagtail<1.10
    from wagtail.wagtailimages.models import get_image_model


MISSING_RESOURCE_CLASS = 'link--missing-resource'
MISSING_RESOURCE_URL = '#'


def HR(props):
    return DOM.create_element('hr')


def Link(props):
    link_type = props.get('linkType', '')
    title = props.get('title')

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
        'href': href
    }

    if title is not None:
        anchor_properties['title'] = title

    return DOM.create_element('a', anchor_properties, props['children'])


def Image(props):
    """
    Inspired by:
    - https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailimages/rich_text.py
    - https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailimages/shortcuts.py
    - https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailimages/formats.py
    """
    image_model = get_image_model()
    alignment = props.get('alignment', 'left')
    alt_text = props.get('altText', '')

    try:
        image = image_model.objects.get(id=props['id'])
    except image_model.DoesNotExist:
        return DOM.create_element('img', {'alt': alt_text})

    image_format = get_image_format(alignment)
    rendition = get_rendition_or_not_found(image, image_format.filter_spec)

    return DOM.create_element('img', dict(rendition.attrs_dict, **{
        'class': image_format.classnames,
        'src': rendition.url,
        'alt': alt_text,
    }))


def Embed(props):
    """
    Inspired by: https://github.com/wagtail/wagtail/blob/master/wagtail/wagtailembeds/rich_text.py
    """
    return DOM.parse_html(embed_to_frontend_html(props['url']))


def Icon(props):
    href = '#icon-%s' % props['name']
    return DOM.create_element(
        'svg',
        {'class': 'icon'},
        DOM.create_element('use', {'xlink:href': href}),
    )


def Document(props):
    document_model = get_document_model()

    try:
        doc = document_model.objects.get(id=props['id'])
        doc_meta = get_document_meta(doc)


    except (document_model.DoesNotExist, AttributeError):
        return DOM.create_element(
            'a',
            {'href': MISSING_RESOURCE_URL, 'class': MISSING_RESOURCE_CLASS + ' file'},
            props['children']
        )

    icon_element = DOM.create_element(Icon, {'name': doc_meta['extension']})

    metadata_element = DOM.create_element(
        'span',
        {'class': 'icon-text__text'},
        props['children'],
        ' '
    )

    size_element = DOM.create_element(
        'span',
        {'class': 'file-size'},
        '({ext} {size})'.format(size=doc_meta['size'], ext=doc_meta['extension'].upper())
    )

    link_item = DOM.create_element('a', {'href': doc.url, 'class': 'icon-text'}, icon_element, metadata_element)

    return DOM.create_element('span', {'class': 'file'}, link_item, size_element)


class BR:
    """
    Replace line breaks (\n) with br tags.
    """
    SEARCH_RE = re.compile(r'\n')

    def render(self, props):
        # Do not process matches inside code blocks.
        if props['block']['type'] == BLOCK_TYPES.CODE:
            return props['children']

        return DOM.create_element('br')
