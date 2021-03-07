from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image, AbstractImage, AbstractRendition

from streams import blocks


class HomePageCarouseImages(Orderable):
    """ ADD SOME NICES IMAGES"""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panel = [
        ImageChooserPanel("carousel_image")
    ]


class HomePage(Page):
    banner_title = models.CharField(
        max_length=100, default="Home Page!"
    )
    introduction = models.TextField(blank=True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL, related_name='+',
    )

    content = StreamField([
        ("cta", blocks.CTABlock()),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("banner_title"),
            FieldPanel("introduction"),
            ImageChooserPanel("banner_image"),
        ], heading="Banner Options"
        ),
        MultiFieldPanel(
            [
                InlinePanel("carousel_images"),
            ], heading="carousel_images"
        ),
        StreamFieldPanel('content'),
    ]
