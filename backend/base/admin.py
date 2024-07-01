
from django.contrib import admin
from .models import Product, Category, Review, Order, OrderItem, ShippingAddress
from .forms import ProductForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('name', 'brand', 'category', 'price', 'countInStock', 'createdAt')
    search_fields = ('name', 'brand', 'category__name')
    list_filter = ('category', 'brand')
    ordering = ('-createdAt',)

    class Media:
        js = ('admin/js/hide_show_fields.js',)

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)