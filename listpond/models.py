from django.db import models
from django.contrib.auth.models import User

class ListLabel(models.Model):
    label = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserLists(models.Model):
    list_content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_lists', null=False, blank=False)
    shared_with_users = models.ManyToManyField(User, related_name='shared_lists', blank=True)
    list_label = models.ForeignKey(ListLabel, on_delete=models.SET_NULL, related_name='label_lists', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ListShare(models.Model):
    requested_by = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    requested_to = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE)
    list = models.ForeignKey(UserLists, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    requested_at = models.DateTimeField(auto_now_add=True)
    request_updated_at = models.DateTimeField(auto_now=True)