from __future__ import absolute_import, unicode_literals

from draftjs_exporter.defaults import BLOCK_MAP

from django.conf import settings
from django.utils. module_loading import import_string

_exporter_config = None


def get_exporter_config():
    global _exporter_config

    if not _exporter_config:
        # Get from settings.
        entity_decorators = getattr(settings, 'DRAFT_EXPORTER_ENTITY_DECORATORS', {})
        block_map = getattr(settings, 'DRAFT_EXPORTER_BLOCK_MAP', BLOCK_MAP)

        # Load classes.
        for block_id, block_class in entity_decorators.items():
            if isinstance(block_class, str):
                entity_decorators[block_id] = import_string(block_class)()

        # Save
        _exporter_config = {
            'entity_decorators': entity_decorators,
            'block_map': block_map
        }

    return _exporter_config
