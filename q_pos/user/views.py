from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Account
from .renderer import AccountRenderer
from ..core.auth import JwtAuth
from .serializer import RegistrationSerializer, LoginSerializer, AccountSerializer, AccountEditSerializer


class RegistrationView(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)
    renderer_classes = (AccountRenderer,)
    serializer_class = RegistrationSerializer

    queryset = Account.objects.all()

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    authentication_classes = ()
    permission_classes = (AllowAny, )
    renderer_classes = (AccountRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountRetrieveUpdateView(RetrieveUpdateAPIView):

    authentication_classes = (JwtAuth, )
    renderer_classes = (AccountRenderer,)
    permission_classes = (IsAuthenticated, )
    serializer_class = AccountSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountEdit(RetrieveUpdateAPIView):
    authentication_classes = (JwtAuth,)
    renderer_classes = (AccountRenderer,)
    permission_classes = (IsAuthenticated,)
    serializer_class = AccountEditSerializer

    def get_queryset(self):
        return Account.objects.filter(pk=self.kwargs['pk'])

