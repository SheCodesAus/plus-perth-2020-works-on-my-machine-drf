from django.http import Http404, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from rest_framework import status, permissions, generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event
from .serializers import EventListSerializer
from .googlecalendar import (
    get_calendar_events,
    create_event,
    update_event,
    delete_event,
)

from mentors.models import MentorProfile


class EventList(APIView):
    def test_api_request(self, user):
        if "credentials" in self.user:
            return self.user
        else:
            raise PermissionDenied

    def get(self, request):
        user = request.user
        # credentials = self.test_api_request(user)
        credentials = user.credentials
        events = get_calendar_events(credentials)
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = request.user
        credentials = user.credentials
        events = get_calendar_events(credentials)
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateEvent(APIView):
    def post(self, request):
        user = request.user
        credentials = user.credentials
        events = create_event(credentials, request.data)
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EventDetail(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventListSerializer(event)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        user = request.user
        credentials = user.credentials
        update_event(credentials, request.data, pk)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        user = request.user
        credentials = user.credentials
        delete_event(credentials, pk)
        get_calendar_events(credentials)
        return Response(status=status.HTTP_204_NO_CONTENT)

#fetch all events that a mentor is invited to
class EventInvitationsList(generics.ListAPIView):
    serializer_class = EventListSerializer

    def get_queryset(self):
        mentor = self.kwargs["pk"]
        profile = MentorProfile.objects.get(pk=mentor)
        return profile.events.all()