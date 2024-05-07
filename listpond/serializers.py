from rest_framework import serializers
from .models import *


class ListLabelSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(read_only=True)

    class Meta:
        model = ListLabel
        fields = "__all__"

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)


class UserListsSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(read_only=True)
    shared_with_users = serializers.CharField(
    allow_blank=True, 
    required=False
)

    class Meta:
        model = UserLists
        fields = "__all__"

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)
    
    def validate_shared_with_users(self, value):
        print(f"{value=}")
        if value:
            shared_with_users_list = [int(user_id) for user_id in value.split(',') if user_id.isdigit()]
            return shared_with_users_list
        return value
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        shared_users = instance.shared_with_users.all()
        representation['shared_with_users'] = [user.username for user in shared_users]
        return representation



class ListShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListShare
        fields = "__all__"
