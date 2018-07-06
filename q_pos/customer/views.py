from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Customer
from ..core.auth import JwtAuth
from .renderer import CustomerRenderer
from .serializer import CustomerRetrieveSerial, CustomerListSerial


class CustomerListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (CustomerRenderer,)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Customer.objects.filter(merchant=self.request.user)

    serializer_class = CustomerListSerial


class CustomerRetrieve(RetrieveUpdateDestroyAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (CustomerRenderer, )
    permission_classes = (IsAuthenticated, )
    serializer_class = CustomerRetrieveSerial

    def get_queryset(self):
        return Customer.objects.filter(merchant=self.request.user)

