from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ..core.auth import JwtAuth

from .models import Employee
from .serializer import EmployeeSerializer, EmployeeCreateSerializer, EmployeeRetrieveUpdateSerial


class EmployeeListCreate(ListCreateAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeSerializer

    def get_queryset(self):
            return Employee.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = EmployeeCreateSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EmployeeRetrieve(RetrieveUpdateDestroyAPIView):
    authentication_classes = (JwtAuth,)
    permission_classes = (IsAuthenticated,)
    serializer_class = (EmployeeRetrieveUpdateSerial)

    def get_queryset(self):
        return Tenant.objects.all()


