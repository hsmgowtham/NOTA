from .serializers import *
from .models import *
from rest_framework import permissions, viewsets  # type: ignore


class ListLabelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to create or view List Labels.
    """
    queryset = ListLabel.objects.all().order_by("-created_at")
    serializer_class = ListLabelSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class UserListsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to create or view Lists
    """

    queryset = UserLists.objects.all().order_by("-created_at")
    serializer_class = UserListsSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListShareViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to create or view shared lists
    """

    queryset = ListShare.objects.all().order_by("-requested_at")
    serializer_class = ListShareSerializer
    permission_classes = [permissions.IsAuthenticated]
