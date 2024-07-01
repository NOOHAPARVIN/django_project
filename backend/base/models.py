from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, default='Tools')

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

     # Additional fields for 'Tools' category
    standard = models.CharField(max_length=200, null=True, blank=True)
    grade = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shape = models.CharField(max_length=200, null=True, blank=True)
    steel_grade = models.CharField(max_length=200, null=True, blank=True)
    surface_finish = models.CharField(max_length=200, null=True, blank=True)
    place_of_origin = models.CharField(max_length=200, null=True, blank=True)
    delivery_time = models.IntegerField(null=True, blank=True)
    model_number = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    application = models.CharField(max_length=200, null=True, blank=True)
    certification = models.CharField(max_length=200, null=True, blank=True)


    def save(self, *args, **kwargs):
        if self.category and self.category.name == 'Tools':
            defaults = {
                'standard': "Default Tool Brand",
                'grade': 5.00,
                'shape': "Default Shape",
                'steel_grade': "Default Steel Grade",
                'surface_finish': "Default Surface Finish",
                'place_of_origin': "Default Place",
                'delivery_time': 10,
                'model_number': "Default Model Number",
                'type': "Default Type",
                'application': "Default Application",
                'certification': "Default Certification",
            }
            for field, default in defaults.items():
                if getattr(self, field) is None:
                    setattr(self, field, default)
        else:
            # Clear tool-specific fields if category is not 'Tools'
            tool_fields = [
                'standard', 'grade', 'shape', 'steel_grade',
                'surface_finish', 'place_of_origin', 'delivery_time',
                'model_number', 'type', 'application', 'certification'
            ]
            for field in tool_fields:
                setattr(self, field, None)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name if self.name else "Unnamed Product"
    
    
   
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reviews')
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f"{self.rating} - {self.product.name if self.product else 'No Product'}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orders')
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f"Order {self._id} by {self.user.username if self.user else 'Anonymous'}"

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='order_items')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='order_items')
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name if self.name else "Unnamed Item"

class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='shipping_address')
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.address if self.address else "No Address"


