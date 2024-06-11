from django.contrib import admin
from .models import Product, Category,Review,Order,OrderItem,ShippingAddress

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'category', 'price', 'countInStock', 'createdAt')
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj and obj.category and obj.category.name == 'Tools':
            form.base_fields['standard'].required = True
            form.base_fields['grade'].required = True
            form.base_fields['shape'].required = True
            form.base_fields['steel_grade'].required = True
            form.base_fields['surface_finish'].required = True
            form.base_fields['place_of_origin'].required = True
            form.base_fields['delivery_time'].required = True
            form.base_fields['model_number'].required = True
            form.base_fields['type'].required = True
            form.base_fields['application'].required = True
            form.base_fields['certification'].required = True
        return form

# Register Product model with ProductAdmin
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Category)
