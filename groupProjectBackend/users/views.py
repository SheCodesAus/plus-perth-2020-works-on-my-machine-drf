from django.http import Http404, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import google.oauth2.credentials
import google_auth_oauthlib.flow
import google.oauth2.credentials
from googleapiclient.discovery import build
from .models import CustomUser
from .serializers import CustomUserSerializer
from .createuser import create_new_user


class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserDetail(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SocialAuth(APIView):
    # This will trigger google to ask the user to sign in with a google account
    def get(self, request):
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            # Use this file for local testing
            # "../client_secret-dev.json",
            # Use this file for deploying to production
            "../../client_secret-production.json",
            scopes=[
                "https://www.googleapis.com/auth/calendar",
                "https://www.googleapis.com/auth/userinfo.email",
                "https://www.googleapis.com/auth/userinfo.profile",
                "https://www.googleapis.com/auth/calendar.readonly",
                "openid",
            ],
        )
        # Use following redirect_uri for local testing
        # flow.redirect_uri = "http://localhost:8000/users/social-auth-success"

        # Use following redirect-uri when deploying to production
        flow.redirect_uri = (
            "https://shecodes-portal-drf.herokuapp.com/users/social-auth-success"
        )

        authorization_url, state = flow.authorization_url(
            # Enable offline access so that you can refresh an access token without
            # re-prompting the user for permission. Recommended for web server apps.
            access_type="offline",
            # Enable incremental authorization. Recommended as a best practice.
            include_granted_scopes="true",
        )
        return HttpResponseRedirect(authorization_url)


class SocialAuthSuccess(APIView):
    # This is where the user actually signs in and grants google access to the scopes
    def get(self, request):
        print("request", request.headers)
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            # Use this file for local testing
            # "../client_secret-dev.json",
            # Use this file for deploying to production
            "../../client_secret-production.json",
            scopes=[
                "https://www.googleapis.com/auth/calendar",
                "https://www.googleapis.com/auth/userinfo.email",
                "https://www.googleapis.com/auth/userinfo.profile",
                "https://www.googleapis.com/auth/calendar.readonly",
                "openid",
            ],
        )
        # Use following redirect_uri for local testing
        # flow.redirect_uri = "http://localhost:8000/users/social-auth-success"

        # Use following redirect-uri when deploying to production
        flow.redirect_uri = (
            "https://shecodes-portal-drf.herokuapp.com/users/social-auth-success"
        )

        authorization_response = request.get_full_path_info()
        flow.fetch_token(authorization_response=authorization_response)

        # The token is generated and we save it to the users session for later use
        credentials = flow.credentials
        request.session["credentials"] = {
            "token": credentials.token,
            "refresh_token": credentials.refresh_token,
            "token_uri": credentials.token_uri,
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
            "scopes": credentials.scopes,
        }
        creds = request.session["credentials"]
        user = create_new_user(self, creds)

        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
