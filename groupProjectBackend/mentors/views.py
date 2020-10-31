
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MentorProfile, MentorProcess
from .serializers import MentorProfileSerializer, MentorProcessSerializer 
from django.shortcuts import render
from django.http import Http404
from rest_framework import status, generics, permissions
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class MentorProcessDetail(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = [IsAuthenticated]
     queryset = MentorProcess.objects.all() 
     serializer_class = MentorProcessSerializer

class MentorProcessList(generics.ListCreateAPIView):
     permission_classes = [IsAuthenticated]
     queryset = MentorProcess.objects.all()
     serializer_class = MentorProcessSerializer

class MentorProfileDetail(generics.RetrieveUpdateDestroyAPIView):
     permission_classes = [IsAuthenticated]
     queryset = MentorProfile.objects.all()
     serializer_class = MentorProfileSerializer

class MentorProfileList(generics.ListCreateAPIView):
     permission_classes = [IsAuthenticated]
     queryset = MentorProfile.objects.all()
     serializer_class = MentorProfileSerializer