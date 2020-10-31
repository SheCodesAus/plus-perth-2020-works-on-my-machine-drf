
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MentorProfile, MentorProcess
from .serializers import MentorProfileSerializer, MentorProcessSerializer 
from django.shortcuts import render
from django.http import Http404
from rest_framework import status, generics, permissions
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly, SAFE_METHODS

class MentorProfileList(APIView):

    def get(self, request):
        mentors = MentorProfile.objects.all()
        serializer = MentorProfileSerializer(mentors, many=True)
        return Response(serializer.data)


class MentorProcessDetail(generics.RetrieveUpdateDestroyAPIView):
#   permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = MentorProcess.objects.all() 
    serializer_class = MentorProcessSerializer

class MentorProcessList(generics.ListCreateAPIView):
#    permission_classes = [IsAuthenticatedOrReadOnly]
     queryset = MentorProcess.objects.all()
     serializer_class = MentorProcessSerializer
