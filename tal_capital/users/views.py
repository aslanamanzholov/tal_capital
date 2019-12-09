from datetime import timezone, datetime

from rest_framework import viewsets, mixins, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import UserSerializer, CreateUserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    http_method_names = ['post', 'get']
    permission_classes = (AllowAny,)


class CapitalObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user, context={'request': request}).data})


class ChangePassword(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args):
        user = User.objects.get(id=self.request.user.id)
        old_password = request.data['old_password']
        if user.check_password(old_password):
            user.set_password(request.data['password'])
            user.save()
            return Response({'detail': 'OK'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Old password does not match'}, status=status.HTTP_400_BAD_REQUEST)
