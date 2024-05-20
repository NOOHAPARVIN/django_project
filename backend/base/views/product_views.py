from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from base.models import Product
from rest_framework import status
from base.serializers import ProductSerializer
# Assuming other necessary imports are here
from rest_framework import viewsets

def get_product_serializer():
    from base.serializers import ProductSerializer
    return ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = get_product_serializer()






@api_view(['GET'])
def getproducts(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getproduct(request,pk):
    product = Product.objects.get(_id=pk)
    serializer=ProductSerializer(Product,many=False)
    return Response(serializer.data)
