from django.contrib import admin

from base.products import Products
from base.category import Category
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
