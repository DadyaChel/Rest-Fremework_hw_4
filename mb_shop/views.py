import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from rest_framework import generics, status
from .seriallisers import CategorySerializers, FirmaSerializers, ProductSerializers
from rest_framework import viewsets


# @csrf_exempt
# def create_product(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         new_tweet = Product.objects.create(**data)
#         json_data = {
#             'name': new_tweet.name,
#             'product_sum': new_tweet.product_sum,
#             'firm': new_tweet.firm.id,
#             'category': new_tweet.category.id,
#         }
#         return JsonResponse(json_data, safe=False)
#     if request.method == 'GET':
#         tweets = Product.objects.all()
#         data = []
#         for tweet in tweets:
#             data.append(
#                 {
#                     'name': tweet.name,
#                     'product_sum': tweet.product_sum
#                 }
#             )
#         json_data = json.dumps(data)
#         return JsonResponse(json_data, safe=False)
#
#
# @csrf_exempt
# def create_firma(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         new_tweet = Firma.objects.create(**data)
#         json_data = {
#             'name': new_tweet.name,
#             'address': new_tweet.address
#         }
#         return JsonResponse(json_data, safe=False)
#     if request.method == 'GET':
#         tweets = Firma.objects.all()
#         data = []
#         for tweet in tweets:
#             data.append(
#                 {
#                     'name': tweet.name,
#                     'address': tweet.address
#                 }
#             )
#         json_data = json.dumps(data)
#         return JsonResponse(json_data, safe=False)
#
#
# @csrf_exempt
# def create_category(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         new_tweet = Category.objects.create(**data)
#         json_data = {
#             'category_name': new_tweet.category_name
#         }
#         return JsonResponse(json_data, safe=False)
#     if request.method == 'GET':
#         tweets = Category.objects.all()
#         data = []
#         for tweet in tweets:
#             data.append(
#                 {
#                     'category_name': tweet.category_name
#                 }
#             )
#         json_data = json.dumps(data)
#         return JsonResponse(json_data, safe=False)


class ProductCreateListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class FirmaCreateListView(generics.ListCreateAPIView):
    queryset = Firma.objects.all()
    serializer_class = FirmaSerializers


class FirmaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Firma.objects.all()
    serializer_class = FirmaSerializers


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class FirmaViewSet(viewsets.ModelViewSet):
    queryset = Firma.objects.all()
    serializer_class = FirmaSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


@api_view(['POST', 'GET'])
def create_product(requests):
    if requests.method == 'POST':
        serializer = ProductSerializers(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if requests.method == "GET":
        message = Product.objects.all()
        serializer = ProductSerializers(instance=message, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_product(request, pk):
    message = generics.get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializers(instance=message)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = ProductSerializers(instance=message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def create_firma(request):
    if request.method == 'POST':
        serializer = FirmaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        message = Firma.objects.all()
        serializer = FirmaSerializers(instance=message, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_firma(request, pk):
    message = generics.get_object_or_404(Firma, pk=pk)
    if request.method == 'GET':
        serializer = FirmaSerializers(instance=message)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = FirmaSerializers(instance=message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def create_category(requests):
    if requests.method == 'POST':
        serializer = CategorySerializers(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if requests.method == "GET":
        message = Category.objects.all()
        serializer = CategorySerializers(instance=message, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_category(request, pk):
    message = generics.get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        serializer = CategorySerializers(instance=message)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = CategorySerializers(instance=message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

