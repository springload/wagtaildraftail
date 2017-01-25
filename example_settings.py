from draftjs_exporter.constants import BLOCK_TYPES, ENTITY_TYPES, INLINE_STYLES
from draftjs_exporter.defaults import BLOCK_MAP

INTRO_BLOCK_ID = 'INTRO_TEXT'
TERMS_BLOCK_ID = 'TERMS_AND_CONDITIONS_TEXT'
SMALL_TEXT_BLOCK_ID = 'SMALL_TEXT'
TINY_TEXT_BLOCK_ID = 'TINY_TEXT'

LOCATION_ENTITY_ID = 'LOCATION'
PAGE_ENTITY_ID = 'PAGE'
STAFF_MEMBER_ENTITY_ID = 'STAFF_MEMBER'

DRAFT_BLOCK_TYPE_H1 = {'label': 'H1', 'type': BLOCK_TYPES.HEADER_ONE}
DRAFT_BLOCK_TYPE_H2 = {'label': 'H2', 'type': BLOCK_TYPES.HEADER_TWO}
DRAFT_BLOCK_TYPE_H3 = {'label': 'H3', 'type': BLOCK_TYPES.HEADER_THREE}
DRAFT_BLOCK_TYPE_H4 = {'label': 'H4', 'type': BLOCK_TYPES.HEADER_FOUR}
DRAFT_BLOCK_TYPE_H5 = {'label': 'H5', 'type': BLOCK_TYPES.HEADER_FIVE}
DRAFT_BLOCK_TYPE_H6 = {'label': 'H6', 'type': BLOCK_TYPES.HEADER_SIX}
DRAFT_BLOCK_TYPE_BLOCKQUOTE = {'label': 'Blockquote', 'type': BLOCK_TYPES.BLOCKQUOTE, 'icon': 'icon-openquote'}
DRAFT_BLOCK_TYPE_UL = {'label': 'UL', 'type': BLOCK_TYPES.UNORDERED_LIST_ITEM, 'icon': 'icon-list-ul'}
DRAFT_BLOCK_TYPE_OL = {'label': 'OL', 'type': BLOCK_TYPES.ORDERED_LIST_ITEM, 'icon': 'icon-list-ol'}
DRAFT_BLOCK_TYPE_INTRO = {'label': 'Intro', 'type': INTRO_BLOCK_ID, 'element': 'div', 'className': 'intro-text'}
DRAFT_BLOCK_TYPE_TERMS = {'label': 'T&Cs', 'type': TERMS_BLOCK_ID, 'element': 'div', 'className': 'legals'}
DRAFT_BLOCK_TYPE_SMALL_TEXT = {
    'label': 'Small', 'type': SMALL_TEXT_BLOCK_ID, 'element': 'div', 'className': 'small-text'}
DRAFT_BLOCK_TYPE_TINY_TEXT = {'label': 'Tiny', 'type': TINY_TEXT_BLOCK_ID, 'element': 'div', 'className': 'tiny-text'}
DRAFT_BLOCK_TYPES = [
    DRAFT_BLOCK_TYPE_H1,
    DRAFT_BLOCK_TYPE_H2,
    DRAFT_BLOCK_TYPE_H3,
    DRAFT_BLOCK_TYPE_H4,
    DRAFT_BLOCK_TYPE_H5,
    DRAFT_BLOCK_TYPE_H6,
    DRAFT_BLOCK_TYPE_BLOCKQUOTE,
    DRAFT_BLOCK_TYPE_UL,
    DRAFT_BLOCK_TYPE_OL,
    DRAFT_BLOCK_TYPE_INTRO,
    DRAFT_BLOCK_TYPE_TERMS,
    DRAFT_BLOCK_TYPE_SMALL_TEXT,
    DRAFT_BLOCK_TYPE_TINY_TEXT,
]

DRAFT_INLINE_STYLE_BOLD = {'label': 'Bold', 'type': INLINE_STYLES.BOLD, 'icon': 'icon-bold'}
DRAFT_INLINE_STYLE_ITALIC = {'label': 'Italic', 'type': INLINE_STYLES.ITALIC, 'icon': 'icon-italic'}
DRAFT_INLINE_STYLE_UNDERLINE = {'label': 'Underline', 'type': INLINE_STYLES.UNDERLINE}
DRAFT_INLINE_STYLE_MONOSPACE = {'label': 'Monospace', 'type': INLINE_STYLES.CODE}
DRAFT_INLINE_STYLE_STRIKETHROUGH = {'label': 'Strikethrough', 'type': INLINE_STYLES.STRIKETHROUGH}
DRAFT_INLINE_STYLES = [
    DRAFT_INLINE_STYLE_BOLD,
    DRAFT_INLINE_STYLE_ITALIC,
    # DRAFT_INLINE_STYLE_UNDERLINE,
    # DRAFT_INLINE_STYLE_MONOSPACE,
    # DRAFT_INLINE_STYLE_STRIKETHROUGH,
]

# It accepts a list of dicts with `label` and `value` keys (e.g. `{'label': 'Full width', 'value': 'fullwidth'}`)
# or a special `__all__` value which will be intercepted and will load all image formats known to Wagtail.
DRAFT_IMAGE_FORMATS = '__all__'

DRAFT_ENTITY_TYPE_IMAGE = {
    'label': 'Image', 'type': ENTITY_TYPES.IMAGE, 'icon': 'icon-image', 'imageFormats': DRAFT_IMAGE_FORMATS}
DRAFT_ENTITY_TYPE_EMBED = {'label': 'Embed', 'type': ENTITY_TYPES.EMBED, 'icon': 'icon-media'}
DRAFT_ENTITY_TYPE_LINK = {'label': 'Link', 'type': ENTITY_TYPES.LINK, 'icon': 'icon-link'}
DRAFT_ENTITY_TYPE_DOCUMENT = {'label': 'Document', 'type': ENTITY_TYPES.DOCUMENT, 'icon': 'icon-doc-full'}
DRAFT_ENTITY_TYPE_LOCATION = {
    'label': 'Location',
    'type': LOCATION_ENTITY_ID,
    'icon': 'icon-site',
    'contentType': 'locations.Location',
    'fields': [{'label': 'Name', 'name': 'name'}],
    'display': 'name'
}
DRAFT_ENTITY_TYPE_PAGE = {
    'label': 'Page',
    'type': PAGE_ENTITY_ID,
    'icon': 'icon-cog',
    'contentType': 'core.BasePage',
    'fields': [{'label': 'Title', 'name': 'title'}],
    'display': 'title'
}
DRAFT_ENTITY_TYPE_STAFF_MEMBER = {
    'label': 'Staff Member',
    'type': STAFF_MEMBER_ENTITY_ID,
    'icon': 'icon-user',
    'contentType': 'staff.BaseStaffMember',
    'fields': [{'label': 'Name', 'name': 'name'}],
    'display': 'name'
}
DRAFT_ENTITY_TYPES = [
    DRAFT_ENTITY_TYPE_IMAGE,
    DRAFT_ENTITY_TYPE_EMBED,
    DRAFT_ENTITY_TYPE_LINK,
    DRAFT_ENTITY_TYPE_DOCUMENT,
    DRAFT_ENTITY_TYPE_LOCATION,
    # DRAFT_ENTITY_TYPE_PAGE
    # DRAFT_ENTITY_TYPE_STAFF_MEMBER
]

WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default_draftjs': {
        'WIDGET': 'wagtailaddons.drafteditor.widgets.JsonTextArea',
        'OPTIONS': {
            'enableHorizontalRule': True,
            'enableLineBreak': False,
            'entityTypes': DRAFT_ENTITY_TYPES,
            'blockTypes': DRAFT_BLOCK_TYPES,
            'inlineStyles': DRAFT_INLINE_STYLES,
        }
    },

    'format_only': {
        'WIDGET': 'wagtailaddons.drafteditor.widgets.JsonTextArea',
        'OPTIONS': {
            'inlineStyles': [
                DRAFT_INLINE_STYLE_BOLD,
                DRAFT_INLINE_STYLE_ITALIC,
            ],
        }
    },

    'format_and_link': {
        'WIDGET': 'wagtailaddons.drafteditor.widgets.JsonTextArea',
        'OPTIONS': {
            'entityTypes': [DRAFT_ENTITY_TYPE_LINK],
            'blockTypes': [
                DRAFT_BLOCK_TYPE_INTRO
            ],
            'inlineStyles': [
                DRAFT_INLINE_STYLE_BOLD,
                DRAFT_INLINE_STYLE_ITALIC,
            ],
        }
    },

    'simple': {
        'WIDGET': 'wagtailaddons.drafteditor.widgets.JsonTextArea',
        'OPTIONS': {
            'enableHorizontalRule': True,
            'enableLineBreak': False,
            'entityTypes': [
                DRAFT_ENTITY_TYPE_LINK,
                DRAFT_ENTITY_TYPE_DOCUMENT,
            ],
            'blockTypes': [
                DRAFT_BLOCK_TYPE_H2,
                DRAFT_BLOCK_TYPE_H3,
                DRAFT_BLOCK_TYPE_H4,
                DRAFT_BLOCK_TYPE_H5,
                DRAFT_BLOCK_TYPE_H6,
                DRAFT_BLOCK_TYPE_INTRO,
                DRAFT_BLOCK_TYPE_SMALL_TEXT,
                DRAFT_BLOCK_TYPE_UL,
                DRAFT_BLOCK_TYPE_OL,
                DRAFT_BLOCK_TYPE_TERMS
            ],
            'inlineStyles': [
                DRAFT_INLINE_STYLE_BOLD,
                DRAFT_INLINE_STYLE_ITALIC,
            ],
        }
    },

    'complex_link': {
        'WIDGET': 'wagtailaddons.drafteditor.widgets.JsonTextArea',
        'OPTIONS': {
            'entityTypes': [DRAFT_ENTITY_TYPE_IMAGE],
            'blockTypes': [
                DRAFT_BLOCK_TYPE_H2,
                DRAFT_BLOCK_TYPE_H3,
                DRAFT_BLOCK_TYPE_H4,
                DRAFT_BLOCK_TYPE_H5,
                DRAFT_BLOCK_TYPE_H6
            ],
            'inlineStyles': [
                DRAFT_INLINE_STYLE_BOLD,
                DRAFT_INLINE_STYLE_ITALIC,
            ],
        }
    },

    'legal_notice': {
        'WIDGET': 'wagtailaddons.drafteditor.widgets.JsonTextArea',
        'OPTIONS': {
            'entityTypes': [
                DRAFT_ENTITY_TYPE_LINK,
                DRAFT_ENTITY_TYPE_DOCUMENT,
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
    ENTITY_TYPES.LINK: 'wagtailaddons.drafteditor.decorators.Link',
    ENTITY_TYPES.DOCUMENT: 'wagtailaddons.drafteditor.decorators.Document',
    ENTITY_TYPES.IMAGE: 'wagtailaddons.drafteditor.decorators.Image',
    ENTITY_TYPES.EMBED: 'wagtailaddons.drafteditor.decorators.Embed',
    ENTITY_TYPES.HORIZONTAL_RULE: 'wagtailaddons.drafteditor.decorators.HR',
    LOCATION_ENTITY_ID: 'wagtailaddons.drafteditor.decorators.Model',
}

DRAFT_EXPORTER_BLOCK_MAP = dict(BLOCK_MAP, **{
    # This causes the element to disappear (fragment tags are stripped)
    # TODO Use specific API provided by draftjs_exporter for this as soon as available.
    BLOCK_TYPES.ATOMIC: {'element': 'fragment'},
    BLOCK_TYPES.HEADER_TWO: {
        'element': ['h2', {'className': 'u-current-color'}],
    },
    BLOCK_TYPES.UNORDERED_LIST_ITEM: {
        'element': 'li',
        'wrapper': ['ul', {'className': 'list-styled'}],
    },
    BLOCK_TYPES.ORDERED_LIST_ITEM: {
        'element': 'li',
        'wrapper': ['ol', {'className': 'list-numbered'}],
    },
    INTRO_BLOCK_ID: {
        'element': ['p', {'className': 'intro'}],
    },
    TERMS_BLOCK_ID: {
        'element': ['p', {'className': 'legals'}],
    },
    SMALL_TEXT_BLOCK_ID: {
        'element': ['p', {'className': 'u-text-'}],
    },
    TINY_TEXT_BLOCK_ID: {
        'element': ['p', {'className': 'u-text--'}],
    },
})
