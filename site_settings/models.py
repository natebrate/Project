from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):
    """List of Links available to the site"""
    instagram = models.URLField(max_length=100)
    link = models.URLField(max_length=100, default='https://www.linkedin.com/in/nathan-brathwaite-80b7a1193/')
    github = models.URLField(max_length=100, default='')
    twitter = models.URLField(max_length=100, default='')
    url = models.URLField(max_length=100, default='', null=True)

    panels = [
        FieldPanel("instagram"),
        FieldPanel("link"),
        FieldPanel("github"),
        FieldPanel("twitter"),
        FieldPanel("url"),
    ]
