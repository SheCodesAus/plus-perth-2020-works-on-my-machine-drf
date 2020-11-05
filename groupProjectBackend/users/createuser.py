import google.oauth2.credentials
import google_auth_oauthlib.flow
from users.models import CustomUser
from googleapiclient.discovery import build
from django.contrib.auth.models import BaseUserManager


def create_new_user(self, creds):
    credentials = google.oauth2.credentials.Credentials(**creds)
    profile = build("oauth2", "v2", credentials=credentials)
    user_info = profile.userinfo().get().execute()
    username = user_info.get("given_name")
    name = user_info.get("given_name")
    email = user_info.get("email")
    user = {
        "email": user_info.get("email"),
        "username": user_info.get("given_name"),
        "user_type": "regular",
    }
    # password = BaseUserManager.make_random_password(self, length=10)

    user, created = CustomUser.objects.get_or_create(
        email=email,
        defaults={
            "username": user_info.get("given_name"),
            "name": user_info.get("given_name"),
            "user_type": "regular",
        },
    )

    return user
