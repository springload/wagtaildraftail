from __future__ import absolute_import, unicode_literals

from draftjs_exporter.constants import BLOCK_TYPES, ENTITY_TYPES, INLINE_STYLES
from draftjs_exporter.defaults import BLOCK_MAP

TERMS_BLOCK_ID = 'TERMS_AND_CONDITIONS_TEXT'

DRAFT_BLOCK_TYPE_H3 = {'label': 'H3', 'type': BLOCK_TYPES.HEADER_THREE}
DRAFT_BLOCK_TYPE_H4 = {'label': 'H4', 'type': BLOCK_TYPES.HEADER_FOUR}
DRAFT_BLOCK_TYPE_UL = {'label': 'UL', 'type': BLOCK_TYPES.UNORDERED_LIST_ITEM, 'icon': 'icon-list-ul'}
DRAFT_BLOCK_TYPE_OL = {'label': 'OL', 'type': BLOCK_TYPES.ORDERED_LIST_ITEM, 'icon': 'icon-list-ol'}
DRAFT_BLOCK_TYPE_TERMS = {'label': 'T&Cs', 'type': TERMS_BLOCK_ID, 'element': 'div', 'className': 'legals'}

DRAFT_INLINE_STYLE_BOLD = {'label': 'Bold', 'type': INLINE_STYLES.BOLD, 'icon': 'icon-bold'}
DRAFT_INLINE_STYLE_ITALIC = {'label': 'Italic', 'type': INLINE_STYLES.ITALIC, 'icon': 'icon-italic'}

# It accepts a list of dicts with `label` and `value` keys (e.g. `{'label': 'Full width', 'value': 'fullwidth'}`)
# or a special `__all__` value which will be intercepted and will load all image formats known to Wagtail.
DRAFT_IMAGE_FORMATS = '__all__'

DRAFT_ENTITY_TYPE_IMAGE = {'label': 'Image', 'type': ENTITY_TYPES.IMAGE, 'icon': 'icon-image', 'imageFormats': DRAFT_IMAGE_FORMATS}
DRAFT_ENTITY_TYPE_EMBED = {'label': 'Embed', 'type': ENTITY_TYPES.EMBED, 'icon': 'icon-media'}
DRAFT_ENTITY_TYPE_LINK = {'label': 'Link', 'type': ENTITY_TYPES.LINK, 'icon': 'icon-link'}
DRAFT_ENTITY_TYPE_DOCUMENT = {'label': 'Document', 'type': ENTITY_TYPES.DOCUMENT, 'icon': 'icon-doc-full'}

WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'simple': {
        'WIDGET': 'wagtaildraftail.widgets.JsonTextArea',
        'OPTIONS': {
            'enableHorizontalRule': True,
            'enableLineBreak': False,
            'entityTypes': [
                DRAFT_ENTITY_TYPE_LINK,
                DRAFT_ENTITY_TYPE_DOCUMENT,
            ],
            'blockTypes': [
                DRAFT_BLOCK_TYPE_H3,
                DRAFT_BLOCK_TYPE_UL,
                DRAFT_BLOCK_TYPE_TERMS,
            ],
            'inlineStyles': [
                DRAFT_INLINE_STYLE_BOLD,
                DRAFT_INLINE_STYLE_ITALIC,
            ],
        }
    },

    'default_draftjs': {
        'WIDGET': 'wagtaildraftail.widgets.JsonTextArea',
        'OPTIONS': {
            'enableHorizontalRule': True,
            'enableLineBreak': False,
            'entityTypes': [
                DRAFT_ENTITY_TYPE_IMAGE,
                DRAFT_ENTITY_TYPE_EMBED,
                DRAFT_ENTITY_TYPE_LINK,
                DRAFT_ENTITY_TYPE_DOCUMENT,
            ],
            'blockTypes': [
                DRAFT_BLOCK_TYPE_H3,
                DRAFT_BLOCK_TYPE_H4,
                DRAFT_BLOCK_TYPE_UL,
                DRAFT_BLOCK_TYPE_OL,
                DRAFT_BLOCK_TYPE_TERMS,
            ],
            'inlineStyles': [
                DRAFT_INLINE_STYLE_BOLD,
                DRAFT_INLINE_STYLE_ITALIC,
            ],
        }
    },

    # Wagtail dependencies
    'default': {
        'WIDGET': 'wagtail.wagtailadmin.rich_text.HalloRichTextArea'
    },

    'custom': {
        'WIDGET': 'wagtail.tests.testapp.rich_text.CustomRichTextArea'
    },
}

DRAFT_EXPORTER_ENTITY_DECORATORS = {
    ENTITY_TYPES.LINK: 'wagtaildraftail.decorators.Link',
    ENTITY_TYPES.DOCUMENT: 'wagtaildraftail.decorators.Document',
    ENTITY_TYPES.IMAGE: 'wagtaildraftail.decorators.Image',
    ENTITY_TYPES.EMBED: 'wagtaildraftail.decorators.Embed',
    ENTITY_TYPES.HORIZONTAL_RULE: 'wagtaildraftail.decorators.HR',
}

DRAFT_EXPORTER_COMPOSITE_DECORATORS = [
    'wagtaildraftail.decorators.BR',
]

DRAFT_EXPORTER_BLOCK_MAP = dict(BLOCK_MAP, **{
    BLOCK_TYPES.UNORDERED_LIST_ITEM: {
        'element': 'li',
        'wrapper': ['ul', {'className': 'list-styled'}],
    },
    BLOCK_TYPES.ORDERED_LIST_ITEM: {
        'element': 'li',
        'wrapper': ['ol', {'className': 'list-numbered'}],
    },
    TERMS_BLOCK_ID: {
        'element': ['p', {'className': 'legals'}],
    },
})
