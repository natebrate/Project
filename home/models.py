import random

from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    banner_title = models.CharField(max_length=100, default="Welcome!")

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
    ]


ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

CATEGORY_CHOICES = (
    ('H', 'Household'),
    ('S', 'Snacks'),
    ('GR', 'Groceries'),
    ('GA', 'Games'),
    ('T', 'Toys'),
    ('OD', 'Outdoors'),

)

# Create your models here.


def generate_unique_code():
    """Generate a random Unique user_profile_id"""
    n = 10
    while True:
        ''.join(["{}".format(random.randint(0, 9)) for _ in range(0, n)])
        if UserProfile.objects.filter(user_profile_id=n).count() == 0:
            break
    return n


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_profile_id = models.CharField(max_length=12, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username


class UserDetails(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    one_click_purchasing = models.BooleanField(default=False, null=True)
    phone = models.CharField(max_length=200, null=True)
    street_address = models.CharField(max_length=100, null=True)
    apartment_address = models.CharField(max_length=100, null=True)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100, null=True)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES, null=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


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

    def __str__(self):
        return self.prodName


class ProductList(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1, null=True)

    def __str__(self):
        return self.quantity


class ProductOrders(models.Model):
    """ The class below gets the users order """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductList)
    start_date = models.DateTimeField(auto_now_add=True, null=True)
    ordered_date = models.DateTimeField(null=True)
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
        return self.user.username
