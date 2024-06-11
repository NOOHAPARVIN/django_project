from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, default='Tools')

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
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

   
    
    def save(self, *args, **kwargs):
        if self.category and self.category.name == 'Tools':
            self.standard = "Default Tool Brand" if not self.standard else self.standard
            self.grade = self.grade or 5.00
            self.shape = self.shape or "Default Shape"
            self.steel_grade = self.steel_grade or "Default Steel Grade"
            self.surface_finish = self.surface_finish or "Default Surface Finish"
            self.place_of_origin = self.place_of_origin or "Default Place"
            self.delivery_time = self.delivery_time or 10
            self.model_number = self.model_number or "Default Model Number"
            self.type = self.type or "Default Type"
            self.application = self.application or "Default Application"
            self.certification = self.certification or "Default Certification"
        super().save(*args, **kwargs)
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
