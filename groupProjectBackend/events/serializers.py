from rest_framework import serializers
from .models import CalendarUrl, Event

class CalendarUrlSerializer(serializers.Serializer):
    calendar_url = serializers.URLField(required=True)

    def create(self, validated_data):
        return CalendarUrl.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.calendar_url = validated_data.get('calendar_url', instance.calendar_url)
        instance.save()
        return instance
    
    def delete(self, validated_data):
        return CalendarUrl.objects.delete(**validated_data)

class EventListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    creator = serializers.ReadOnlyField()
    event_name = serializers.CharField(max_length=200)
    event_start = serializers.DateTimeField()
    event_end = serializers.DateTimeField()