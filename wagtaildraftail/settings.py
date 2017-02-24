from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.utils. module_loading import import_string
from draftjs_exporter.defaults import BLOCK_MAP


_exporter_config = None


def get_exporter_config():
    global _exporter_config

    if not _exporter_config:
        # Get from settings.
        entity_decorators = getattr(settings, 'DRAFT_EXPORTER_ENTITY_DECORATORS', {})
        composite_decorators = getattr(settings, 'DRAFT_EXPORTER_COMPOSITE_DECORATORS', [])
        block_map = getattr(settings, 'DRAFT_EXPORTER_BLOCK_MAP', BLOCK_MAP)

        # Load classes.
        for entity_id, decorator in entity_decorators.items():
            entity_decorators[entity_id] = import_string(decorator)

        # Save
        _exporter_config = {
            'entity_decorators': entity_decorators,
            'composite_decorators': [import_string(decorator) for decorator in composite_decorators],
            'block_map': block_map
        }

    return _exporter_config
