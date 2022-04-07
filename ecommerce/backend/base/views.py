from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .products import products


@api_view(['GET'])
def getProducts(request):

    op = {product['_id']: product for product in products}
    print(op.get('1'))
    return Response(products)

# Create your views here.
@api_view(['GET'])
def getProduct(request,pk):

    op = {product['_id']: product for product in products}
    product_found = (op.get(pk))
    return Response(product_found)


def getRoutes(request):
    return JsonResponse("Hello", safe=False)
