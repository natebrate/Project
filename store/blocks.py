"""Add your blocks here"""
from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock


class IntroBlock(blocks.StructBlock):
    banner_title = blocks.CharBlock(max_length=200, default="Welcome to the store")
    intro = blocks.TextBlock(blank=True, max_length=500)

    class Meta:
        template = "streams/intro_block.html"
        icon = "Edit Body"
        label = "Introduction Body"


class BodyBlock(blocks.StructBlock):
    heading = blocks.RichTextBlock(required=True, help_text="Add Your Heading")
    image = ImageChooserBlock(required=False, help_text="Add Your Image")
    paragraph = blocks.RichTextBlock(required=True, max_length=40, help_text="Add Your Paragraph")

    class Meta:
        template = "streams/body_block.html"
        icon = "Edit Body"
        label = "Store Body"


class FoodBlocks(blocks.StructBlock):
    """Card with image, text and buttons"""
    title = blocks.CharBlock(required=True, help_text="Add Your Title")

    foodCard = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("title", blocks.TextBlock(required=True, max_length=200)),
                ("text", blocks.RichTextBlock(required=True, max_length=200)),
                ("Price", blocks.IntegerBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/food_block.html"
        icon = "placeholder"
        label = "Product Cards"
