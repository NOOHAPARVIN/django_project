from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status, viewsets
from base.models import Product
from base.serializers import ProductSerializer

def get_product_serializer():
    from base.serializers import ProductSerializer
    return ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = get_product_serializer()

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = get_object_or_404(Product, _id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user

    product = Product.objects.create(
        user=user,
        name='Sample Name',
        price=0,
        brand='Sample Brand',
        countInStock=0,
        category='Sample Category',
        description=''
    )

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    product = get_object_or_404(Product, _id=pk)
    data = request.data

    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.brand = data.get('brand', product.brand)
    product.countInStock = data.get('countInStock', product.countInStock)
    product.category = data.get('category', product.category)
    product.description = data.get('description', product.description)

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = get_object_or_404(Product, _id=pk)
    product.delete()
    return Response('Product Deleted', status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def uploadImage(request):
    data = request.data
    product_id = data.get('product_id')
    product = get_object_or_404(Product, _id=product_id)

    product.image = request.FILES.get('image')
    product.save()

    return Response('Image was uploaded')
