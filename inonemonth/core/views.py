from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import generics


User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
