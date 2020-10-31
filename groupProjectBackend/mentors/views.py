
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MentorProfile, MentorProcess
from .serializers import MentorProfileSerializer, MentorProcessSerializer 
from django.shortcuts import render
from django.http import Http404
from rest_framework import status, generics, permissions
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class MentorProcessDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = MentorProcess.objects.all() 
     serializer_class = MentorProcessSerializer

class MentorProcessList(generics.ListCreateAPIView):
     queryset = MentorProcess.objects.all()
     serializer_class = MentorProcessSerializer

class MentorProfileDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = MentorProfile.objects.all()
     serializer_class = MentorProfileSerializer

class MentorProfileList(generics.ListCreateAPIView):
     queryset = MentorProfile.objects.all()
     serializer_class = MentorProfileSerializer