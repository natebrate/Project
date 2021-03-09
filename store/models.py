import random

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from . import blocks


class StorePage(Page):
    """The Actual Page to buy Food from other food pages will inherit this page"""
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    intro = StreamField(
        [
            ('intro_block', blocks.IntroBlock()),
        ],
        null=True,
        blank=True
    )

    content = StreamField(
        [
            ('body_block', blocks.BodyBlock()),
            ('foodCard', blocks.FoodBlocks()),
        ],
        null=True,
        blank=True
    )

    product = models.ForeignKey(
        'Products',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        # Panels in here
        MultiFieldPanel([
            ImageChooserPanel("image"),
            StreamFieldPanel("intro"),
            StreamFieldPanel("content"),
            SnippetChooserPanel('product'),
        ], heading="Store Options"
        )
    ]

    class Meta:
        verbose_name = "Store Page"
        verbose_name_plural = "Store Pages"


"""
    Models for the store create below
"""

"""CHOICE FOR DATABASE"""
ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

CATEGORY_CHOICES = (
    ('M', 'Meat'),
    ('ST', 'Starch'),
    ('F', 'Fruit'),
    ('ME', 'Meal'),
    ('D', 'Drink'),
    ('SN', 'Snacks'),

)

ORDER_TYPE = (
    ('D', 'Delivery'),
    ('TO', 'Take Out'),
    ('IS', 'In Store'),
)


# Create your models here.


def generate_unique_code():
    """Generate a random Unique user_profile_id"""
    n = 10
    while True:
        ''.join(["{}".format(random.randint(0, 9)) for _ in range(0, n)])
        if UserProfile.objects.filter(user_id=n).count() == 0:
            break
    return n


def generate_food_id():
    """Generate a random Unique Product ID"""
    n = 10
    while True:
        ''.join(["{}".format(random.randint(0, 9)) for _ in range(0, n)])
        if Products.objects.filter(prodID=n).count() == 0:
            break
    return n


@register_snippet
class UserProfile(models.Model):
    """User Profile Model"""
    user_name = models.CharField(max_length=100, null=True)
    user_id = models.IntegerField(null=True, unique=True)
    email = models.CharField(max_length=200, null=True, unique=True)
    phone_number = models.CharField(max_length=200, null=True)
    date_created = models.DateField(null=True)

    panels = [
        FieldPanel('user_name'),
        FieldPanel('user_id'),
        FieldPanel('email'),
        FieldPanel('phone_number'),
        FieldPanel('date_created'),
    ]

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = 'User Profiles'


@register_snippet
class UserInformation(models.Model):
    """Separate the User information that isn't required initially"""
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    one_click_purchasing = models.BooleanField(default=False, null=True)
    street_address = models.CharField(max_length=100, null=True)
    apartment_address = models.CharField(max_length=100, null=True, default='')
    zip = models.CharField(max_length=100, null=True)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES, null=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.user_name

    panels = [
        FieldPanel('user'),
        FieldPanel('one_click_purchasing'),
        FieldPanel('street_address'),
        FieldPanel('apartment_address'),
        FieldPanel('zip'),
        FieldPanel('address_type'),
        FieldPanel('default'),
    ]

    class Meta:
        verbose_name = "User Information"


@register_snippet
class Products(models.Model):
    """List of products available to purchase"""
    title = models.CharField(max_length=100, null=True)
    prodID = models.CharField(max_length=200, null=False, primary_key=True, unique=True)
    price = models.FloatField(null=True)
    prodName = models.CharField(max_length=200, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    quantity = models.IntegerField(null=True)
    description = models.TextField(null=True)
    date_created = models.DateField(null=True)
    product_image = models.ForeignKey('wagtailimages.Image', null=True, blank=False,
                                      on_delete=models.SET_NULL,
                                      related_name='+')
    panels = [
        FieldPanel('title'),
        FieldPanel('prodID'),
        FieldPanel('price'),
        FieldPanel('prodName'),
        FieldPanel('category'),
        FieldPanel('quantity'),
        FieldPanel('description'),
        FieldPanel('date_created'),
        ImageChooserPanel('product_image')
    ]

    def __str__(self):
        return self.prodName

    class Meta:
        verbose_name_plural = 'Store Products'


@register_snippet
class ProductList(models.Model):
    """For the user basket"""
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1, null=True)

    def __str__(self):
        return self.product.prodName

    class Meta:
        verbose_name_plural = 'Product List'


@register_snippet
class ProductOrders(models.Model):
    """ The class below gets the user's order """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductList)
    start_date = models.DateTimeField(auto_now_add=True, null=True)
    ordered_date = models.DateTimeField(null=True)
    order_type = models.CharField(choices=ORDER_TYPE, max_length=3, default="")
    ordered = models.BooleanField(default=False, null=True)

    '''
        1. Item added to cart
        2. Adding a billing address
        (Failed checkout)
        3. Payment
        (Preprocessing, processing, packaging etc.)
        4. Being delivered
        5. Received
        6. Refunds
        '''

    def __str__(self):
        return self.user.user_name

    class Meta:
        verbose_name_plural = 'Customer Orders'
