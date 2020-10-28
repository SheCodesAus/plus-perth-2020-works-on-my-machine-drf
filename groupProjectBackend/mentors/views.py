
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MentorProfile, MentorProcess
from .serializers import MentorProfileSerializer, MentorProcessSerializer 

class MentorProfileList(APIView):

    def get(self, request):
        mentors = MentorProfile.objects.all()
        serializer = MentorProfileSerializer(mentors, many=True)
        return Response(serializer.data)
       