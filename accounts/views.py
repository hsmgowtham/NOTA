from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets  # type: ignore
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import (
    BlacklistedToken,
    OutstandingToken,
)


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
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
        # queryset just for schema generation metadata
            return User.objects.none()

    def get_object(self):
        user_id = self.kwargs.get("pk")
        return get_object_or_404(User, pk=user_id)


class UpdateProfileView(generics.UpdateAPIView):
    """
    API endpoint that allows users to update their profile
    """

    serializer_class = UpdateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
        # queryset just for schema generation metadata
            return User.objects.none()

    def get_object(self):
        user_id = self.kwargs.get("pk")
        return get_object_or_404(User, pk=user_id)


class LogoutView(APIView):
    """
    API endpoint that Logouts the user
    """

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    """
    API endpoint that Logouts the user from all devices
    """

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
