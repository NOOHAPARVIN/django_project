from django.shortcuts import render, get_object_or_404
from base.models import Category

# View to list all categories
def category_list(request):
    categories = Category.get_all_categories()
    return render(request, 'categories/category_list.html', {'categories': categories})

# View to show details of a single category
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'categories/category_detail.html', {'category': category})
