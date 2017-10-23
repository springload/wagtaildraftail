from __future__ import absolute_import, unicode_literals

from draftjs_exporter.constants import BLOCK_TYPES, ENTITY_TYPES, INLINE_STYLES
from wagtail.wagtailcore import hooks

from .features import BlockFeature, BooleanFeature, EntityFeature, ImageFeature, InlineStyleFeature


@hooks.register('register_rich_text_features')
def register_core_draftail_features(features):
    features.register_editor_plugin(
        'draftail', 'hr', BooleanFeature('enableHorizontalRule')
    )

    features.register_editor_plugin(
        'draftail', 'br', BooleanFeature('enableLineBreak')
    )

    features.register_editor_plugin(
        'draftail', 'h1', BlockFeature({'label': 'H1', 'type': BLOCK_TYPES.HEADER_ONE})
    )
    features.register_editor_plugin(
        'draftail', 'h2', BlockFeature({'label': 'H2', 'type': BLOCK_TYPES.HEADER_TWO})
    )
    features.register_editor_plugin(
        'draftail', 'h3', BlockFeature({'label': 'H3', 'type': BLOCK_TYPES.HEADER_THREE})
    )
    features.register_editor_plugin(
        'draftail', 'h4', BlockFeature({'label': 'H4', 'type': BLOCK_TYPES.HEADER_FOUR})
    )
    features.register_editor_plugin(
        'draftail', 'h5', BlockFeature({'label': 'H5', 'type': BLOCK_TYPES.HEADER_FIVE})
    )
    features.register_editor_plugin(
        'draftail', 'h6', BlockFeature({'label': 'H6', 'type': BLOCK_TYPES.HEADER_SIX})
    )
    features.register_editor_plugin(
        'draftail', 'ul', BlockFeature({
            'label': 'UL', 'type': BLOCK_TYPES.UNORDERED_LIST_ITEM, 'icon': 'icon-list-ul'
        })
    )
    features.register_editor_plugin(
        'draftail', 'ol', BlockFeature({
            'label': 'OL', 'type': BLOCK_TYPES.ORDERED_LIST_ITEM, 'icon': 'icon-list-ol'
        })
    )

    features.register_editor_plugin(
        'draftail', 'bold', InlineStyleFeature({
            'label': 'Bold', 'type': INLINE_STYLES.BOLD, 'icon': 'icon-bold'
        })
    )
    features.register_editor_plugin(
        'draftail', 'italic', InlineStyleFeature({
            'label': 'Italic', 'type': INLINE_STYLES.ITALIC, 'icon': 'icon-italic'
        })
    )

    features.register_editor_plugin(
        'draftail', 'link', EntityFeature({
            'label': 'Link',
            'type': ENTITY_TYPES.LINK,
            'icon': 'icon-link',
            'source': 'LinkSource',
            'decorator': 'Link',
        })
    )

    features.register_editor_plugin(
        'draftail', 'document-link', EntityFeature({
            'label': 'Document',
            'type': ENTITY_TYPES.DOCUMENT,
            'icon': 'icon-doc-full',
            'source': 'DocumentSource',
            'decorator': 'Document',
        })
    )

    features.register_editor_plugin(
        'draftail', 'image', ImageFeature()
    )

    features.register_editor_plugin(
        'draftail', 'embed', EntityFeature({
            'label': 'Embed',
            'type': ENTITY_TYPES.EMBED,
            'icon': 'icon-media',
            'source': 'EmbedSource',
            'decorator': 'Embed',
        })
    )
