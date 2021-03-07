from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.models import Image, AbstractImage, AbstractRendition

from . import blocks


class FlexPage(Page):
    """
        Flex Page Model
     """
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlocks()),
            ("full_richtext", blocks.RichtextBlock()),
            ("simple_richtext", blocks.SimpleRichtextBlock()),
            ("cards", blocks.CardBlock()),
        ],
        null=True,
        blank=True
    )
    subtitle = models.CharField(
        max_length=200,
        default="Subtitle Page"
    )

    something = models.TextField(
        max_length=200,
        default="Subtitle Page",
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name_plural = 'Flex Pages'
