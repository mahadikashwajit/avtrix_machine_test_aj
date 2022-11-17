from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            return Product.objects.filter(product__icontains=search)
        else:
            return Product.objects.all()
        

class ProductPostAPIView(APIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        search = self.request.GET.get('search')
        return Product.objects.filter(product__icontains=search)

    def post(self, request, *args, **kwargs):
        request_data = self.request.data
        search = request_data['search']
        queryset = Product.objects.filter(product__icontains=search)[:5]
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
