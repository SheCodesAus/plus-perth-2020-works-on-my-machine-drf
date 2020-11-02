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


class EventList(APIView):
    def test_api_request(self, request):
        if "credentials" in self.request.session:
            return self.request.session["credentials"]
        else:
            raise PermissionDenied

    def get(self, request):
        breakpoint()
        credentials = self.test_api_request(request)
        events = Event.objects.all()
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        credentials = request.session["credentials"]
        events = get_calendar_events(credentials)
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateEvent(APIView):
    def post(self, request):
        credentials = request.session["credentials"]
        print(request.data)
        create_event(credentials, request.data)
        return HttpResponseRedirect("/events")


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
        credentials = request.session["credentials"]
        update_event(credentials, request.data, pk)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        credentials = request.session["credentials"]
        delete_event(credentials, pk)
        get_calendar_events(credentials)
        return Response(status=status.HTTP_204_NO_CONTENT)
