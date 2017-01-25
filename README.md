# wagtaildraftail

> Draft.js editor for Wagtail, built upon [draftail](https://github.com/springload/draftail) and [draftjs_exporter](https://github.com/springload/draftjs_exporter).

**This is pre-alpha software. It is made available publicly for review purposes only, and is not expected to work out of the box.**

## Usage

### With Pages

Add the field to your page object:

```python
from wagtaildraftail.fields import DraftailTextField

class MyPage(Page):
    body = DraftailTextField()

    panels = [
        FieldPanel('body')
    ]
```

Apply the `draft_text` filter into your template (make sure it's available to your template engine):

```html
{{ page.body|draft_text }}
```

### With StreamField

```python
from wagtaildraftail.blocks import DraftailTextBlock

class MyStructBlock(StructBlock):
    body = DraftailTextBlock()
```

### Editor Configuration

Both `DraftailTextField` and `DraftailTextBlock` accept a string as keyword argument `editor` for a per field customisation.

Wagtail will look for a `WAGTAILADMIN_RICH_TEXT_EDITORS` constants in the settings (currently defined in `kiwibank_public/settings/grains/rich_text.py`), find the requested editor, load the defined widget and pass the options (if defined) to it.

Each editor defined in `WAGTAILADMIN_RICH_TEXT_EDITORS` is a dictionary with 2 keys:, `WIDGET` (mandatory) and `OPTIONS` (optional).

- `WIDGET` is a mandatory string set to the widget to use
    - should always be set to `wagtaildraftail.widgets.JsonTextArea` (or a subclass of it) to work with Draft.js content
- `OPTIONS` is a dictionary which follows the format of [Draftail configuration options](https://github.com/springload/draftail#usage).
    - Draftail options which are JavaScript values are hydrated at runtime in `client/wagtaildraftail.js`

**WARNING:** The `type` key for `blockTypes`, `inlineStyles` and `entityTypes` shouldn't be changed. It is what defines how content is rendered, and is saved as a JSON blob in the database which would make migrations really painful.

**WARNING:** All the blocks/styles/entities defined in the editor config should have been configured to render properly in the [exporter config](#exporter-configuration).

## Creating new content formats

### Creating blocks and inline styles

There are only two configurations to update:

- The [editor configuration](#editor-configuration) to display the controls in the editor.
- The [exporter configuration](#exporter-configuration) to be able to render the new block on pages.

This will apply your new block/style to the selected text in the editor and render it properly in the template.

### Creating entities

Entities are useful when page content requires both textual content written in the editor, and data from other sources (typically the CMS, an API, or a more advanced control in the editor).

Creating entities requires the same configuration changes as blocks and inline styles, but it is also necessary to write:

- React components to define how the entities are visually rendered in the editor.
- React components to manage the entity's data. In Wagtail, this would typically be a chooser modal.
- Python code to define how the entities are visually rendered on the page.

### Exporter Configuration

Base configuration is defined in `kiwibank_public.settings.grains.rich_text`:

- `DRAFT_EXPORTER_ENTITY_DECORATORS` is a dictionary where:
    - The key is the entity type as defined by the `type` value of `entityTypes` in the [editor configuration](#editor-configuration).
    - The value is the dotted module path of a Python class responsible for rendering this entity.
- `DRAFT_EXPORTER_BLOCK_MAP` is a dictionary where:
    - The key is the block type (or name) as defined by the `type` value of `blockTypes` in the [editor configuration](#editor-configuration).
    - The value is a dictionary which defines how the block is to be rendered.

Please refer to the [`drafts_exporter` usage information](https://github.com/springload/draftjs_exporter#usage) for more details.

To access the full configuration in a module, use `wagtaildraftail.settings.get_exporter_config`.
