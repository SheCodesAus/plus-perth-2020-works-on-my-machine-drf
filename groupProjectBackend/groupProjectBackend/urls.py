from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

# from users.views import ConvertToken

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("rest_framework_social_oauth2.urls")),
    # path("auth/convert-token", ConvertToken.as_view(), name="convert-token"),
    path("", include("events.urls")),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("mentors/", include("mentors.urls")),
]
