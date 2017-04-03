from __future__ import absolute_import, unicode_literals

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page

from wagtaildraftail.fields import DraftailTextField


class HomePage(Page):
    body_draftail = DraftailTextField(blank=True)
    body_hallo = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body_draftail', classname="full"),
        FieldPanel('body_hallo', classname="full"),
    ]
