from rest_framework.viewsets import ModelViewSet
from product.models import StoreProduct
from .serializer import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = StoreProduct.objects.all()
    serializer_class = ProductSerializer