from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Inventory
from ..core.auth import JwtAuth
from .serializer import RetrieveUpdateSerial, ListCreateSerial
from .renderer import InventoryRenderer


class InventoryListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    permission_classes = (IsAuthenticated, )
    renderer_classes = (InventoryRenderer, )
    serializer_class = ListCreateSerial

    def get_queryset(self):
        return Inventory.objects.filter(merchant=self.request.user.id)

class InventoryRetrieveUpdate(RetrieveUpdateAPIView):
    authentication_classes = (JwtAuth, )
    authentication_classes = (JwtAuth, )
    permission_classes = (IsAuthenticated, )
    serializer_class = RetrieveUpdateSerial

    def get_queryset(self):
        return Inventory.objects.filter(merchant=self.request.user.id)


