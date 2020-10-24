from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    user_type = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
    def delete(self, validated_data):
        return User.objects.delete(**validated_data)