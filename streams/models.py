from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.models import Image, AbstractImage, AbstractRendition

from . import blocks


class FlexPage(Page):
    """ Flex Page Model """
    body = StreamField(
        [
            ("rich_text", blocks.RichtextBlock()),
        ],
        null=True,
        blank=True
    )
    content = StreamField(
        [
            ("title_and_text", blocks.TitleAndTextBlocks()),
            ("cards", blocks.CardBlock()),
            ("button", blocks.ButtonBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name_plural = 'Flex Pages'
