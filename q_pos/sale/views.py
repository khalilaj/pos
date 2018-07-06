from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..core.auth import JwtAuth
from .models import Sale, SaleProduct
from .renderer import SaleRenderer, SaleItemRenderer
from .serializer import SaleListCreateSerializer, SaleRetrieveSerializer


class SalesListCreateView (ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    permission_classes = (IsAuthenticated, )
    renderer_classes = (SaleRenderer,)
    serializer_class = SaleListCreateSerializer

    def get_queryset(self):
        return Sale.objects.filter(merchant=self.request.user.id)


class SaleRetrieveView (RetrieveUpdateDestroyAPIView):

    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = (SaleRenderer,)
    serializer_class = SaleRetrieveSerializer

    def get_queryset(self):
        return Sale.objects.filter(merchant=self.request.user.id)
