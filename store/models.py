import random

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image, AbstractImage, AbstractRendition
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class StorePage(Page):
    """The Actual Page to buy Food from other food pages will inherit this page"""
    banner_title = models.CharField(
        max_length=200,
        default="Welcome to the store"
    )
    intro = models.TextField(blank=True, max_length=500)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    product = models.ForeignKey(
        'Products',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("intro"),
        ImageChooserPanel("image"),
        SnippetChooserPanel('product'),

    ]


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
    user_name = models.CharField(max_length=100, null=False)
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
        verbose_name_plural = 'Customer (User) Information'


@register_snippet
class UserDetails(models.Model):
    """Separate the User information that isn't required initially"""
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE)
    one_click_purchasing = models.BooleanField(default=False, null=True)
    street_address = models.CharField(max_length=100, null=True)
    apartment_address = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=100, null=True)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES, null=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = 'Additional User Information'


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
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1, null=True)

    def __str__(self):
        return self.product

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
        return self.user

    class Meta:
        verbose_name_plural = 'Customer Orders'
