from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MentorProfile, MentorProcess
from .serializers import MentorProfileSerializer, MentorProcessSerializer
from django.shortcuts import render
from django.http import Http404
from rest_framework import status, generics, permissions
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticated,
    SAFE_METHODS,
)
from .addmentorscript import create_new_mentor


class MentorProcessDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MentorProcess.objects.all()
    serializer_class = MentorProcessSerializer

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return MentorProcessSerializer
        return MentorProcessStaffSerializer

class MentorProcessList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MentorProcess.objects.all()
    serializer_class = MentorProcessSerializer

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

class MentorProfile(generics.RetrieveAPIView):
    serializer_class = MentorProfileSerializer
    def get_object(self):
        mentor_id = self.kwargs['pk']
        try:
            return MentorProfile.objects.get(owner=user_id)
        except MentorProfile.DoesNotExist:
            raise Http404