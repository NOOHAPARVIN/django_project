from django.shortcuts import render, get_object_or_404
from base.models import Category
from django.http import JsonResponse
from django.forms import model_to_dict

def category_list(request):
    categories = Category.objects.all()
    data = {'categories': list(categories.values())}
    return JsonResponse(data)

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    data = {'category': model_to_dict(category)}
    return JsonResponse(data)