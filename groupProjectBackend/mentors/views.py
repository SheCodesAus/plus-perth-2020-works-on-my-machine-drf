from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MentorProfile, MentorProcess
from .serializers import MentorProfileSerializer, MentorProcessSerializer, MentorProcessStaffSerializer
# from .permissions import BlacklistPermission
from django.shortcuts import render
from django.http import Http404
from rest_framework import status, generics, permissions
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser, SAFE_METHODS
from .addmentorscript import create_new_mentor

class MentorProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MentorProcess.objects.all()
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return MentorProcessSerializer
        return MentorProcessStaffSerializer

class MentorProcessList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MentorProcess.objects.all()
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return MentorProcessSerializer
        return MentorProcessStaffSerializer

class MentorProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

class MentorProfileList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MentorProfile.objects.all()
    serializer_class = MentorProfileSerializer

class MentorFileUpload(APIView):
    def post(self, request):
        mentors = create_new_mentor()
        return Response(data=mentors, status=status.HTTP_201_CREATED)