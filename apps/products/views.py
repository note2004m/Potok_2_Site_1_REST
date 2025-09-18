from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.products.models import Product
from apps.products.serializers import ProductSerializer, ProductCreateUpdateSerializer

# Create your views here.
class ProductAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        if self.request.method in ("POST", "PUT"):
            return ProductCreateUpdateSerializer
        return ProductSerializer