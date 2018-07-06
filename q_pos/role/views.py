from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Role
from ..core.auth import JwtAuth
from .renderer import RoleRenderer
from .serializer import RoleRetrieveSerial, RoleListSerial


class RoleListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (RoleRenderer,)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Role.objects.filter(merchant=self.request.user)

    serializer_class = RoleListSerial


class RoleRetrieve(RetrieveUpdateDestroyAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (RoleRenderer, )
    permission_classes = (IsAuthenticated, )

    queryset = Role.objects.all()
    serializer_class = RoleRetrieveSerial
