from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import PaymentMethod
from ..core.auth import JwtAuth
from .renderer import PaymentMethodRenderer
from .serializer import PaymentMethodRetrieveSerial, PaymentMethodListSerial


class PaymentMethodListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth,)
    renderer_classes = (PaymentMethodRenderer,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return PaymentMethod.objects.filter(merchant=self.request.user)

    serializer_class = PaymentMethodListSerial


class PaymentMethodRetrieve(RetrieveUpdateDestroyAPIView):

    authentication_classes = (JwtAuth,)
    renderer_classes = (PaymentMethodRenderer,)
    permission_classes = (IsAuthenticated,)

    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodRetrieveSerial
