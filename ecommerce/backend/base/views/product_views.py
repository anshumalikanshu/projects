from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
 
 

# from .products import products
from base.models import Product
from base.serializer import ProductSerializer


@api_view(['GET'])
def getProducts(request):

    products = Product.objects.all()
    serialozer = ProductSerializer(products, many=True)
    return Response(serialozer.data)

# Create your views here.


@api_view(['GET'])
def getProduct(request, pk):

    # op = {product['_id']: product for product in products}
    # product_found = (op.get(pk))
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)
