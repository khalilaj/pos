from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Product
from ..core.auth import JwtAuth
from .renderer import ProductRenderer
from .serializer import ProductRetrieveSerial, ProductListSerial


class ProductListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    permission_classes = (IsAuthenticated, )
    renderer_classes = (ProductRenderer,)
    serializer_class = ProductListSerial

    def get_queryset(self):
        return Product.objects.filter(merchant=self.request.user.id)


class ProductRetrieve(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = (JwtAuth, )
    renderer_classes = (ProductRenderer, )
    permission_classes = (IsAuthenticated, )
    serializer_class = ProductRetrieveSerial

    def get_queryset(self):
        return Product.objects.filter(merchant=self.request.user.id)

    def perform_destroy(self, instance):
        # print(instance.delete)

                instance.delete()

