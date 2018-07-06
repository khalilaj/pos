from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ..core.auth import JwtAuth
from .permissions import MerchantAccessPermission

from .models import Merchant
from .serializer import MerchantSerializer, MerchantCreateSerializer, MerchantRetrieveUpdateSerial


class MerchantListCreate(ListCreateAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, MerchantAccessPermission,)
    serializer_class = MerchantSerializer

    def get_queryset(self):
            return Merchant.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = MerchantCreateSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MerchantRetrieve(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated, MerchantAccessPermission)
    serializer_class = MerchantRetrieveUpdateSerial

    def get_queryset(self):
            return Merchant.objects.all()


