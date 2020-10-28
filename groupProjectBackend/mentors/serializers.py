from rest_framework import serializers
from .models import MentorProfile, MentorProcess

class MentorProfileSerializer(serializer.ModelSerializer):
    id = serializers.ReadOnlyField()
    mentor_name = serializers.CharField(max_length=200)
    mentor_email = serializers.CharField(max_length=200)
    phone_number = serializers.IntegerField()
    location = serializers.CharField(max_length=200)
    skills = serializers.CharField(max_length=200)
    mentor_type = serializers.CharField(max_length=200)
    one_day_workshop = serializers.BooleanField()

    def create(self, validated_data):
        return MentorProfile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)

    def delete(self, validated_data):
        return MentorProfile.objects.delete(**validated_data)


class MentorProcessSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    mentor_name = serializers.ForeignKey()
    step_one = serializers.BooleanField()
    step_two = serializers.BooleanField()
    step_three = serializers.BooleanField()
    step_four = serializers.BooleanField()
    step_five = serializers.BooleanField()
    step_six = serializers.BooleanField()
    step_seven = serializers.BooleanField()
    step_eight = serializers.BooleanField()

    def create(self, validated_data):
        return MentorProcess.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)

    def delete(self, validated_data):
        return MentorProfile.objects.delete(**validated_data)
   
    
    