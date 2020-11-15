from rest_framework import serializers
from .models import Event, Attendance
from mentors.models import MentorProfile
from mentors.serializers import MentorProfileSerializer


class AttendanceSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=20)
    mentor = MentorProfileSerializer()


class EventListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    creator = serializers.ReadOnlyField(source="creator.id")
    event_city = serializers.CharField(max_length=200)
    event_name = serializers.CharField(max_length=200)
    event_type = serializers.CharField(max_length=200)
    event_start = serializers.DateTimeField()
    event_end = serializers.DateTimeField()
    event_location = serializers.CharField(max_length=200)
    all_day = serializers.BooleanField()
    mentor_list = serializers.SlugRelatedField(
        many=True, slug_field="mentor_name", queryset=MentorProfile.objects.all()
    )
    attendance_set = AttendanceSerializer(many=True)

    # def delete(self, validated_data):
    #     return Event.objects.delete(**validated_data)
