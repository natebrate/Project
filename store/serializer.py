from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
import graphene


def products(request):
    product = Products.objects.all()

    return product
