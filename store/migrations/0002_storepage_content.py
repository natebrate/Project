# Generated by Django 3.1.7 on 2021-03-07 12:52

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storepage',
            name='content',
            field=wagtail.core.fields.StreamField([('body_block', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.RichTextBlock(help_text='Add Your Heading', required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Add Your Image', required=True)), ('paragraph', wagtail.core.blocks.RichTextBlock(help_text='Add Your Paragraph', max_length=40, required=True))])), ('foodCard', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add Your Title', required=True)), ('foodCard', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=200, required=True)), ('Price', wagtail.core.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))]))], blank=True, null=True),
        ),
    ]
