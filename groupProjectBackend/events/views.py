from django.http import Http404
from rest_framework import status, permissions, generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, CalendarUrl
from .serializers import CalendarUrlSerializer, EventListSerializer
from .calendarscript import get_events
from .googlecalendar import getCalendarEvents


class AddCalendar(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CalendarUrlSerializer(data=request.data)
        if serializer.is_valid():
            url, created = CalendarUrl.objects.get_or_create(
                calendar_url=serializer.validated_data["calendar_url"]
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class EventList(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)

    def test_api_request(self, request):
        if "credentials" not in request.session:
            return HttpResponseRedirect("/users/social-auth")

    def post(self, request, *args, **kwargs):
        credentials = request.session["credentials"]
        # test_api_request(credentials)
        events = getCalendarEvents(credentials)
        # serializer = EventListSerializer(events, many=True)
        return Response(
            # serializer.data,
            status=status.HTTP_201_CREATED
        )


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

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventListSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)