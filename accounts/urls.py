# accounts/urls.py
from django.urls import path, include
from rest_framework import routers # type: ignore
from . import views
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
) 

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password'),

    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
