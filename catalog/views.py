from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.permissions import IsAdminOrReadOnly
from .models import Brand, Category, Product
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category', 'brand').all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]