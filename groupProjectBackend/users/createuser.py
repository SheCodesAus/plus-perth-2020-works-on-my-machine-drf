import google.oauth2.credentials
import google_auth_oauthlib.flow
from users.models import CustomUser
from googleapiclient.discovery import build
from django.contrib.auth.models import BaseUserManager

import logging

logger = logging.getLogger("django.server")


def create_new_user(self, creds):
    creds_dict = {
        "token": creds.token,
        "refresh_token": creds.refresh_token,
        "token_uri": creds.token_uri,
        "client_id": creds.client_id,
        "client_secret": creds.client_secret,
        "scopes": creds.scopes,
    }
    credentials = google.oauth2.credentials.Credentials(**creds_dict)
    profile = build("oauth2", "v2", credentials=credentials)
    creds = creds.to_json()
    user_info = profile.userinfo().get().execute()
    username = user_info.get("given_name")
    name = user_info.get("given_name")
    email = user_info.get("email")
    user = {
        "email": user_info.get("email"),
        "username": user_info.get("given_name"),
        "user_type": "regular",
        "credentials": creds,
    }

    user, created = CustomUser.objects.get_or_create(
        email=email,
        defaults={
            "username": user_info.get("given_name"),
            "name": user_info.get("given_name"),
            "user_type": "regular",
            "credentials": creds,
        },
    )

    logger.info(user.credentials)
    return user
