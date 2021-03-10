from django.db import models
from django.shortcuts import render
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.images.models import Image, AbstractImage, AbstractRendition

from streams import blocks


class HomePageCarouseImages(Orderable):
    """ ADD SOME NICE IMAGES"""

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


class HomePage(RoutablePageMixin, Page):
    """Home page"""
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
                InlinePanel("carousel_images", max_num=5, min_num=1, label="Image"),
            ], heading="carousel_images"
        ),
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Pages'

    @route(r'^subscribe/$')
    def the_subscribe_page(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context['a_special_test'] = "Hello and Welcome"

        return render(request, "home/subscribe.html", context)
