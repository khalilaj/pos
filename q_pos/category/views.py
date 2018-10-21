from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Category
from ..core.auth import JwtAuth
from .renderer import CategoryRenderer
from .serializer import CategoryRetrieveSerial, CategoryListSerial


class CategoryListCreate(ListCreateAPIView):

    authentication_classes = (JwtAuth,)
    renderer_classes = (CategoryRenderer,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CategoryListSerial

    def get_queryset(self):
        return Category.objects.filter(merchant=self.request.user.id)


class CategoryRetrieve(RetrieveUpdateDestroyAPIView):

    authentication_classes = (JwtAuth,)
    renderer_classes = (CategoryRenderer,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CategoryRetrieveSerial

    def get_queryset(self):
        return Category.objects.filter(merchant=self.request.user.id)
