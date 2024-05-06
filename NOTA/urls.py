from django.urls import include, path

urlpatterns = [
    path('accounts/', include('accounts.urls')),  # Include user-related URLs from the 'accounts' app
]