from __future__ import absolute_import, unicode_literals

import re

from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from draftjs_exporter.constants import BLOCK_TYPES
from draftjs_exporter.dom import DOM
from draftjs_exporter.style_state import camel_to_dash
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.models import get_document_model
from wagtail.wagtailembeds.format import embed_to_frontend_html
from wagtail.wagtailimages.formats import get_image_format
from wagtail.wagtailimages.models import get_image_model
from wagtail.wagtailimages.shortcuts import get_rendition_or_not_found

from .utilities import get_document_meta

MISSING_RESOURCE_CLASS = 'link--missing-resource'
MISSING_RESOURCE_URL = '#'


def HR(props):
    return DOM.create_element('hr')


class Link:
    def render(self, props):
        data = props.get('data', {})

        if 'id' in data:
            try:
                page = Page.objects.get(id=data['id'])
                href = page.url
            except Page.DoesNotExist:
                href = data.get('url', MISSING_RESOURCE_URL)
        else:
            href = data.get('url', MISSING_RESOURCE_URL)

        return DOM.create_element('a', {
            'href': href,
            'title': data.get('title'),
        }, props['children'])


class Model:
    """
    Link to a resource.

    The resource model is expected to implement an `url` method,
    which accepts no parameters and return the relative url to the resource.
    """

    def render(self, props):
        data = props.get('data', {})

        try:
            model_class = apps.get_model(data['contentType'])
            model = model_class.objects.get(pk=data['id'])
            href = model.url()
            class_name = 'link--{model}'.format(model=camel_to_dash(model_class.__name__))

        # Component is missing `contentType` or `id` key(s); or model is missing `url` attribute.
        # Those are developer errors and shouldn't be silenced.
        except (KeyError, AttributeError):
            raise

        # Content-type or object do not exist.
        except (LookupError, ObjectDoesNotExist):
            href = MISSING_RESOURCE_URL
            class_name = MISSING_RESOURCE_CLASS

        return DOM.create_element('a', {'className': class_name, 'href': href}, props['children'])


class Image:
    """
    Inspired by:
    - https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailimages/rich_text.py
    - https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailimages/shortcuts.py
    - https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailimages/formats.py
    """
    def render(self, props):
        image_model = get_image_model()
        alignment = props['data'].get('alignment', 'left')
        alt_text = props['data'].get('altText', '')

        try:
            image = image_model.objects.get(id=props['data']['id'])
        except image_model.DoesNotExist:
            return DOM.create_element('img', {'alt': alt_text})

        image_format = get_image_format(alignment)
        rendition = get_rendition_or_not_found(image, image_format.filter_spec)

        return DOM.create_element('img', dict(rendition.attrs_dict, **{
            'class': image_format.classnames,
            'src': rendition.url,
            'alt': alt_text,
        }))


class Embed:
    """
    Inspired by: https://github.com/torchbox/wagtail/blob/master/wagtail/wagtailembeds/rich_text.py
    """
    def render(self, props):
        return DOM.parse_html(embed_to_frontend_html(props['data']['url']))


def Icon(props):
    href = '#icon-%s' % props['name']
    return DOM.create_element(
        'svg',
        {'class': 'icon'},
        DOM.create_element('use', {'xlink:href': href}),
    )


class Document:
    def render(self, props):
        document_model = get_document_model()

        try:
            doc = document_model.objects.get(id=props['data']['id'])
            doc_meta = get_document_meta(doc)


        except (document_model.DoesNotExist, AttributeError):
            return DOM.create_element(
                'a',
                {'href': MISSING_RESOURCE_URL, 'className': MISSING_RESOURCE_CLASS + ' file'},
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
        if props['block_type'] == BLOCK_TYPES.CODE:
            return props['children']

        return DOM.create_element('br')
