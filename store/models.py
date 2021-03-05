from django.db import models

# Create your models here.

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class StorePage(Page):
    banner_title = models.CharField(
        max_length=100, default="Store Front!"
    )
    introduction = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("introduction")
    ]
