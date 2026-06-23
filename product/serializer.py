from rest_framework.serializers import Serializer
from rest_framework.generics import ListAPIView
from .models import StoreProduct
class ProductSerializer ():
    class Meta:
        model=StoreProduct
        field='__all__'