from rest_framework import serializers
from .models import CalendarUrl, Event
from mentors.models import MentorProfile


class CalendarUrlSerializer(serializers.Serializer):
    calendar_url = serializers.URLField(required=True)

    def create(self, validated_data):
        return CalendarUrl.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.calendar_url = validated_data.get(
            "calendar_url", instance.calendar_url
        )
        instance.save()
        return instance

    def delete(self, validated_data):
        return CalendarUrl.objects.delete(**validated_data)


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

    # def create(self, validated_data):
    #     mentors = validated_data.pop('mentor_list')
    #     event = Event.objects.create(**validated_data)
    #     event.mentor_list.set(mentors)
    #     event.save()
    #     return event

    # def update(self, instance, validated_data):
    #     instance.creator = validated_data.get('creator', instance.creator)
    #     instance.event_city = validated_data.get('event_city', instance.event_city)
    #     instance.event_name = validated_data.get('event_name', instance.event_name)
    #     instance.event_type = validated_data.get('event_type', instance.event_type)
    #     instance.event_start = validated_data.get('event_start', instance.event_start)
    #     instance.event_end = validated_data.get('event_end', instance.event_end)
    #     instance.event_location = validated_data.get('event_location', instance.event_location)
    #     instance.save()
    #     return instance

    def delete(self, validated_data):
        return Event.objects.delete(**validated_data)