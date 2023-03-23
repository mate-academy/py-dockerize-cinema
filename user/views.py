from rest_framework import generics
<<<<<<< HEAD
from rest_framework.permissions import IsAuthenticated
=======
from rest_framework.permissions import IsAuthenticated, AllowAny
>>>>>>> 52f3c262dc599376d6ab612bf9e70249ff34fe08
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import User
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self) -> User:
        return self.request.user
