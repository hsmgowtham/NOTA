from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets  # type: ignore
from rest_framework import generics


from .serializers import (
    RegisterUserSerializer,
    ChangePasswordSerializer,
    UpdateProfileSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChangePasswordView(generics.UpdateAPIView):
    """
    API endpoint that allows users to update their password
    """

    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs.get("pk")
        return get_object_or_404(User, pk=user_id)


class UpdateProfileView(generics.UpdateAPIView):
    """
    API endpoint that allows users to update their profile
    """

    serializer_class = UpdateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs.get("pk")
        return get_object_or_404(User, pk=user_id)
