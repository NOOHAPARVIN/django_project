# update_categories.py

from django.core.management.base import BaseCommand
from base.models import Category, Product

class Command(BaseCommand):
    help = 'Update category for existing products'

    def handle(self, *args, **kwargs):
        try:
            valid_category = Category.objects.get(name='Tools')
            products_to_update = Product.objects.filter(category__name='Sample Category')
            for product in products_to_update:
                product.category = valid_category
                product.save()
            self.stdout.write(self.style.SUCCESS('Successfully updated categories for existing products.'))
        except Category.DoesNotExist:
            self.stderr.write(self.style.ERROR('Category matching query does not exist.'))
