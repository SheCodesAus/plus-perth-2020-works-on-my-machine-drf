from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MentorProfile, MentorProcess
from .serializers import MentorProfileSerializer, MentorProcessSerializer
from django.shortcuts import render
from django.http import Http404
from rest_framework import status, generics, permissions
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticatedOrReadOnly,
    SAFE_METHODS,
)
from .addmentorscript import create_new_mentor


class MentorProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    #   permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = MentorProcess.objects.all()
    serializer_class = MentorProcessSerializer


class MentorProcessList(generics.ListAPIView):
    #    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = MentorProcess.objects.all()
    serializer_class = MentorProcessSerializer


class MentorProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    #   permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer


class MentorProfileList(generics.ListCreateAPIView):
    #    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer


class MentorFileUpload(APIView):
    def post(self, request):
        mentors = create_new_mentor()
        return Response(data=mentors, status=status.HTTP_201_CREATED)