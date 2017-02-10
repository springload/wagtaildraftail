.. image:: https://travis-ci.org/springload/wagtaildraftail.svg?branch=master
   :target: https://travis-ci.org/springload/wagtaildraftail
.. image:: https://img.shields.io/pypi/v/wagtaildraftail.svg
   :target: https://pypi.python.org/pypi/wagtaildraftail
.. image:: https://coveralls.io/repos/github/springload/wagtaildraftail/badge.svg?branch=master
   :target: https://coveralls.io/github/springload/wagtaildraftail?branch=master

wagtaildraftail 🐦📝🍸
=======================

    Draft.js editor for Wagtail, built upon `Draftail`_ and `draftjs\_exporter`_.

**This is alpha software, use at your own risk.**

Installation
------------

Grab the package from pip with, ``pip install wagtaildraftail``, then add ``wagtaildraftail`` as an app in your Django settings.

Usage
-----

With Pages
~~~~~~~~~~

Add the field to your page object:

.. code:: python

    from wagtaildraftail.fields import DraftailTextField

    class MyPage(Page):
        body = DraftailTextField()

        panels = [
            FieldPanel('body')
        ]

Apply the ``draft_text`` filter into your template (make sure it’s available to your template engine):

.. code:: html

    {{ page.body|draft_text }}

With StreamField
~~~~~~~~~~~~~~~~

.. code:: python

    from wagtaildraftail.blocks import DraftailTextBlock

    class MyStructBlock(StructBlock):
        body = DraftailTextBlock()

Configuration
~~~~~~~~~~~~~~~~~~~~

Both ``DraftailTextField`` and ``DraftailTextBlock`` accept a string as keyword argument ``editor`` for a per field customisation.

Wagtail will look for a ``WAGTAILADMIN_RICH_TEXT_EDITORS`` constants in the settings, find the requested editor, load the defined widget and pass the options (if defined) to it.

Each editor defined in ``WAGTAILADMIN_RICH_TEXT_EDITORS`` is a dictionary with 2 keys:, ``WIDGET`` (mandatory) and ``OPTIONS`` (optional).

-  ``WIDGET`` is a mandatory string set to the widget to use
   -  should always be set to ``wagtaildraftail.widgets.JsonTextArea`` (or a subclass of it) to work with Draft.js content
-  ``OPTIONS`` is a dictionary which follows the format of `Draftail configuration options`_.
   -  Draftail options which are JavaScript values are hydrated at runtime in ``client/wagtaildraftail.js``

**WARNING:** The ``type`` key for ``blockTypes``, ``inlineStyles`` and ``entityTypes`` shouldn’t be changed. It is what defines how content is rendered, and is saved as a JSON blob in the database which would make migrations really painful.

**WARNING:** All the blocks/styles/entities defined in the editor config should have been configured to render properly in the `exporter config`_.

Here is a sample configuration file. This should live in your Django settings.

.. code:: python

    from wagtaildraftail.constants import BLOCK_TYPES, ENTITY_TYPES, INLINE_STYLES
    from wagtaildraftail.defaults import BLOCK_MAP

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

        'extended': {
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

        'format_only': {
            'WIDGET': 'wagtaildraftail.widgets.JsonTextArea',
            'OPTIONS': {
                'inlineStyles': [
                    DRAFT_INLINE_STYLE_BOLD,
                    DRAFT_INLINE_STYLE_ITALIC,
                ],
            }
        },

        'format_and_link': {
            'WIDGET': 'wagtaildraftail.widgets.JsonTextArea',
            'OPTIONS': {
                'entityTypes': [
                    DRAFT_ENTITY_TYPE_LINK,
                ],
                'blockTypes': [
                    DRAFT_BLOCK_TYPE_TERMS
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

    DRAFT_EXPORTER_BLOCK_MAP = dict(BLOCK_MAP, **{
        # This causes the element to disappear (fragment tags are stripped)
        # TODO Use specific API provided by wagtaildraftail for this as soon as available.
        BLOCK_TYPES.ATOMIC: {'element': 'fragment'},
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

Creating new content formats
----------------------------

TODO

Creating blocks and inline styles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TODO

Creating entities
~~~~~~~~~~~~~~~~~

TODO

Development
-----------

Installation
~~~~~~~~~~~~

    Requirements: ``virtualenv``, ``pyenv``, ``twine``

.. code:: sh

    git clone git@github.com:springload/wagtaildraftail.git
    cd wagtaildraftail/
    virtualenv .venv
    source ./.venv/bin/activate
    make init
    # Install the git hooks
    ./.githooks/deploy
    # Install all tested python versions
    pyenv install 2.7.11 && pyenv install 3.3.6 && pyenv install 3.4.4 && pyenv install 3.5.1
    pyenv global system 2.7.11 3.3.6 3.4.4 3.5.1

Commands
~~~~~~~~

.. code:: sh

    make help            # See what commands are available.
    make init            # Install dependencies and initialise for development.
    make publish         # Publishes a new version to pypi.

Debugging
~~~~~~~~~

TODO

Releases
~~~~~~~~

*  Update the `changelog`_.
*  Update the version number in ``wagtaildraftail/__init__.py``, following semver.
*  ``git release vx.y.z``
*  ``make publish`` (confirm, and enter your password)
*  Go to https://pypi.python.org/pypi/wagtaildraftail and check that all is well

Documentation
-------------

    See the `docs`_ folder

.. _Draftail: https://github.com/springload/draftail
.. _draftjs\_exporter: https://github.com/springload/wagtaildraftail
.. _Draftail configuration options: https://github.com/springload/draftail#usage
.. _exporter config: #exporter-configuration
.. _changelog: https://github.com/springload/wagtaildraftail/CHANGELOG.md
.. _docs: https://github.com/springload/wagtaildraftail/docs/