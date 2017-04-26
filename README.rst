.. image:: https://travis-ci.org/springload/wagtaildraftail.svg?branch=master
   :target: https://travis-ci.org/springload/wagtaildraftail
.. image:: https://img.shields.io/pypi/v/wagtaildraftail.svg
   :target: https://pypi.python.org/pypi/wagtaildraftail
.. image:: https://coveralls.io/repos/github/springload/wagtaildraftail/badge.svg?branch=master
   :target: https://coveralls.io/github/springload/wagtaildraftail?branch=master

wagtaildraftail 🐦📝🍸
=======================

    Draft.js editor for Wagtail, built upon `Draftail <https://github.com/springload/draftail>`_ and `draftjs_exporter <https://github.com/springload/draftjs_exporter>`_.

**This is alpha software, use at your own risk. Do not use in production (yet).**

Check out `Awesome Wagtail <https://github.com/springload/awesome-wagtail>`_ for more awesome packages and resources from the Wagtail community.

Installation
------------

Grab the package from pip with ``pip install wagtaildraftail``, then add ``wagtaildraftail`` as an app in your Django settings.

Usage
-----

    There is a basic test site set up in the ``tests`` folder for reference.

With Pages
~~~~~~~~~~

First, add a Draftail field to some of your pages. Here is an example:

.. code:: python

    from wagtaildraftail.fields import DraftailTextField

    class MyPage(Page):
        body = DraftailTextField(blank=True)

        panels = [
            FieldPanel('body')
        ]

Then, when displaying those fields, use the ``richtext`` filter in the templates.

.. code:: html

    {% load wagtailcore_tags %}

    {% block content %}
        {{ page.body|richtext }}
    {% endblock %}

With StreamField
~~~~~~~~~~~~~~~~

Here is an example using the ready-made block:

.. code:: python

    from wagtaildraftail.blocks import DraftailTextBlock

    class MyStructBlock(StructBlock):
        body = DraftailTextBlock()

Configuration
~~~~~~~~~~~~~

Both ``DraftailTextField`` and ``DraftailTextBlock`` accept a string as keyword argument ``editor`` for a per field customisation.

Wagtail will look for a ``WAGTAILADMIN_RICH_TEXT_EDITORS`` constants in the settings, find the requested editor, load the defined widget and pass the options (if defined) to it.

Each editor defined in ``WAGTAILADMIN_RICH_TEXT_EDITORS`` is a dictionary with 2 keys:, ``WIDGET`` (mandatory) and ``OPTIONS`` (optional).

-  ``WIDGET`` is a mandatory string set to the widget to use
   -  should always be set to ``wagtaildraftail.widgets.DraftailTextArea`` (or a subclass of it) to work with Draft.js content
-  ``OPTIONS`` is a dictionary which follows the format of `Draftail configuration options <https://github.com/springload/draftail#usage>`_.
   -  Draftail options which are JavaScript values are hydrated at runtime in ``client/wagtaildraftail.js``

**WARNING:** The ``type`` key for ``blockTypes``, ``inlineStyles`` and ``entityTypes`` shouldn’t be changed. It is what defines how content is rendered, and is saved as a JSON blob in the database which would make migrations really painful.

**WARNING:** All the blocks/styles/entities defined in the editor config should have been configured to render properly in the `exporter config <#exporter-configuration>`_.

Here is a sample configuration file. This should live in your Django settings.

.. code:: python

    from draftjs_exporter.constants import BLOCK_TYPES, ENTITY_TYPES, INLINE_STYLES
    from draftjs_exporter.defaults import BLOCK_MAP

    TERMS_BLOCK_ID = 'TERMS_AND_CONDITIONS_TEXT'

    DRAFT_BLOCK_TYPE_H3 = {'label': 'H3', 'type': BLOCK_TYPES.HEADER_THREE}
    DRAFT_BLOCK_TYPE_H4 = {'label': 'H4', 'type': BLOCK_TYPES.HEADER_FOUR}
    DRAFT_BLOCK_TYPE_UL = {'label': 'UL', 'type': BLOCK_TYPES.UNORDERED_LIST_ITEM, 'icon': 'icon-list-ul'}
    DRAFT_BLOCK_TYPE_OL = {'label': 'OL', 'type': BLOCK_TYPES.ORDERED_LIST_ITEM, 'icon': 'icon-list-ol'}
    DRAFT_BLOCK_TYPE_TERMS = {'label': 'T&Cs', 'type': TERMS_BLOCK_ID, 'element': 'div', 'class': 'legals'}

    DRAFT_INLINE_STYLE_BOLD = {'label': 'Bold', 'type': INLINE_STYLES.BOLD, 'icon': 'icon-bold'}
    DRAFT_INLINE_STYLE_ITALIC = {'label': 'Italic', 'type': INLINE_STYLES.ITALIC, 'icon': 'icon-italic'}

    # It accepts a list of dicts with `label` and `value` keys (e.g. `{'label': 'Full width', 'value': 'fullwidth'}`)
    # or a special `__all__` value which will be intercepted and will load all image formats known to Wagtail.
    DRAFT_IMAGE_FORMATS = '__all__'

    DRAFT_ENTITY_TYPE_IMAGE = {
        'label': 'Image',
        'type': ENTITY_TYPES.IMAGE,
        'icon': 'icon-image',
        'imageFormats': DRAFT_IMAGE_FORMATS,
        'source': 'ImageSource',
        'decorator': 'Image',
    }
    DRAFT_ENTITY_TYPE_EMBED = {
        'label': 'Embed',
        'type': ENTITY_TYPES.EMBED,
        'icon': 'icon-media',
        'source': 'EmbedSource',
        'decorator': 'Embed',
    }
    DRAFT_ENTITY_TYPE_LINK = {
        'label': 'Link',
        'type': ENTITY_TYPES.LINK,
        'icon': 'icon-link',
        'source': 'LinkSource',
        'decorator': 'Link',
    }
    DRAFT_ENTITY_TYPE_DOCUMENT = {
        'label': 'Document',
        'type': ENTITY_TYPES.DOCUMENT,
        'icon': 'icon-doc-full',
        'source': 'DocumentSource',
        'decorator': 'Document',
    }

    WAGTAILADMIN_RICH_TEXT_EDITORS = {
        'default_draftail': {
            'WIDGET': 'wagtaildraftail.widgets.DraftailTextArea',
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
                ],
                'inlineStyles': [
                    DRAFT_INLINE_STYLE_BOLD,
                    DRAFT_INLINE_STYLE_ITALIC,
                ],
            }
        },

        'format_and_link': {
            'WIDGET': 'wagtaildraftail.widgets.DraftailTextArea',
            'OPTIONS': {
                'entityTypes': [
                    DRAFT_ENTITY_TYPE_LINK,
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
            'wrapper': 'ul',
            'wrapper_props': {'class': 'list-styled'},
        },
        BLOCK_TYPES.ORDERED_LIST_ITEM: {
            'element': 'li',
            'wrapper': 'ol',
            'wrapper_props': {'class': 'list-numbered'},
        },
        TERMS_BLOCK_ID: {
            'element': 'p',
            'props': {'class': 'legals'},
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

An entity basically needs 4 elements:
-  a page ``decorator``.
-  an editor ``decorator``.
-  an editor ``source``.
-  an editor ``strategy``.

Decorators define how the content needs to be displayed on the site's pages, as well as within the editor.
- For the pages, they are defined in Python with ``draftjs_exporter``. Refer to the dedicated documentation on [the draftjs_exporter README](https://github.com/springload/draftjs_exporter#custom-components).
- For the editor, they are defined in JS/React with ``draftail``. Refer to the dedicated documentation on [the Draftail README](https://github.com/springload/draftail).

Sources define the interface (usually a modal) through which the user will select an entity to insert into the editor.

Strategies allow the editor to identify entities when it is loaded. Strategies are optional as the default one works fine in most cases.

Both sources and strategies are defined in JS/React with ``draftail``. Refer to the dedicated documentation on [the Draftail README](https://github.com/springload/draftail).

To register decorators, sources or strategies to ``wagtaildraftail``, use the corresponding register function:

.. code:: javascript

    window.wagtailDraftail.registerDecorators({ LinkDecorator, ButtonDecorator });
    window.wagtailDraftail.registerSources({ LinkSource });
    window.wagtailDraftail.registerStrategies({ LinkStrategy });

Note: In order for ``wagtailDraftail`` and its register functions to be available in the global ``window`` namespace, make sure that ``wagtaildraftail`` appears before any other app which will try to register an entity in ``INSTALED_APPS``.


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
    # Install all tested python versions
    pyenv install 2.7.11 && pyenv install 3.3.6 && pyenv install 3.4.4 && pyenv install 3.5.1
    pyenv global system 2.7.11 3.3.6 3.4.4 3.5.1

Commands
~~~~~~~~

.. code:: sh

    make help            # See what commands are available.
    make init            # Install dependencies and initialise for development.
    make start           # Starts the development server and compilation tools.
    make lint            # Lint the project.
    make load-data       # Prepares the database for usage.
    make test            # Test the project.
    make test-coverage   # Run the tests while generating test coverage data.
    make test-ci         # Continuous integration test suite.
    make clean-pyc       # Remove Python file artifacts.
    make dist            # Compile the JS and CSS for release.
    make publish         # Publishes a new version to pypi.

Debugging
~~~~~~~~~

To get up and running,

.. code:: sh

    # Set up the development environment.
    make init
    # Start the development server.
    make start
    # If necessary, start the JS compilation watch
    npm run start

There are testing and linting tasks available both in the Makefile (Python) and package.json (JS).

Updating test data
~~~~~~~~~~~~~~~~~~

Here are useful commands:

.. code:: sh

    # Create new migrations from changes to the project.
    python tests/manage.py makemigrations
    # "Reset" the database.
    rm db.sqlite3
    # Generate fixtures from DB data. Remember to clean them up so they do not overlap with data from migrations.
    python tests/manage.py dumpdata > tests/fixtures/test_data.json

Releases
~~~~~~~~

*  Make a new branch for the release of the new version.
*  Update the `CHANGELOG <https://github.com/springload/wagtaildraftail/CHANGELOG.md>`_.
*  Update the version number in ``wagtaildraftail/__init__.py`` and ``package.json``, following semver.
*  Make a PR and squash merge it.
*  Back on master with the PR merged, use ``make publish`` (confirm, and enter your password).
*  Finally, go to GitHub and create a release and a tag for the new version.
*  Done!

Documentation
-------------

    See the `docs <https://github.com/springload/wagtaildraftail/docs/>`_ folder
