from django.urls import path, include
from rest_framework import routers  # type: ignore
from . import views

router = routers.DefaultRouter()
router.register(r"list_labels", views.ListLabelViewSet)
router.register(r"user_lists", views.UserListsViewSet)
router.register(r"list_share", views.ListShareViewSet)

urlpatterns = [path("", include(router.urls))]
