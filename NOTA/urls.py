from django.urls import include, path
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="NOTA",
        default_version='v1',
        description="Simple List Sharing App",
        terms_of_service="",
        contact=openapi.Contact(email="hsmgowtham@gmail.com"),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('NOTA.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("accounts/", include("accounts.urls")),
    path("listpond/", include("listpond.urls")),
]
