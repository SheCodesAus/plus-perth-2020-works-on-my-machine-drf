
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MentorProfile, MentorProcess
from .serializers import MentorProfileSerializer, MentorProcessSerializer


class MentorProfileList(APIView):

    def get(self, request):
        mentors = MentorProfile.objects.all()
        serializer = MentorProfileSerializer(mentors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MentorProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class MentorProfileDetails(APIView):

    def get(self, request, pk):
        mentor = self.get_object(pk)
        serializer = MentorDetailSerializer(mentor)
        return Response(serializer.data)

    