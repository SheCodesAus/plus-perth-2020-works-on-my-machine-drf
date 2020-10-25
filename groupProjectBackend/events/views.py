from django.http import Http404
from rest_framework import status, permissions, generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, CalendarUrl
from .serializers import CalendarUrlSerializer, EventListSerializer
from .calendarscript import get_events

class AddCalendar(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CalendarUrlSerializer(data = request.data)
        if serializer.is_valid():
            url, created = CalendarUrl.objects.get_or_create(calendar_url = serializer.validated_data['calendar_url'])
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )   
        
class Events(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventListSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        url = CalendarUrl.objects.get(pk=1).calendar_url
        events = get_events(url)
        serializer = EventListSerializer(events, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

