
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

    def get_object(self, pk):
        try:
            mentor = MentorProfile.objects.get(pk=pk)
            self.check_object_permissions(self.request, mentor)
            return mentor
        except user.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mentor = self.get_object(pk)
        serializer = MentorDetailSerializer(mentor)
        return Response(serializer.data)

    def put(self, request, pk):
        mentor = self.get_object(pk)
        data = request.data
        serializer = MentorProfileSerializer(
            instance=user,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        mentor = self.get_object(pk)
        if mentor:
            mentor.delete()
            return Response({"status":"ok"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
