from django.contrib.auth.models import Group, User
from rest_framework import serializers

from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['url', 'username', 'first_name', 'email', 'groups']
        fields = "__all__"
    
    def create(self, validated_data):
        # Update the date_joined field to the current UTC time if not provided
        if 'date_joined' not in validated_data:
            validated_data['date_joined'] = timezone.now()
        return super().create(validated_data)
    
class GroupSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Group
        fields = ['url', 'name']