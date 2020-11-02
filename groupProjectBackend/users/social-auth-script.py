# import google.oauth2.credentials
# import google_auth_oauthlib.flow
# from

# def auth_with_google(request)
#     flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
#             "../client_secret.json",
#             scopes=[
#                 "https://www.googleapis.com/auth/calendar",
#                 "https://www.googleapis.com/auth/userinfo.email",
#                 "https://www.googleapis.com/auth/userinfo.profile",
#                 "https://www.googleapis.com/auth/calendar.readonly",
#                 "openid",
#             ],
#         )
#         flow.redirect_uri = "http://localhost:8000/users/social-auth-success"
#         authorization_url, state = flow.authorization_url(
#             # Enable offline access so that you can refresh an access token without
#             # re-prompting the user for permission. Recommended for web server apps.
#             access_type="offline",
#             # Enable incremental authorization. Recommended as a best practice.
#             include_granted_scopes="true",
#         )
#     return authorization_url

# def get_google_creds(request):
#     def get(self, request):
#     flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
#         "../client_secret.json",
#         scopes=[
#             "https://www.googleapis.com/auth/calendar",
#             "https://www.googleapis.com/auth/userinfo.email",
#             "https://www.googleapis.com/auth/userinfo.profile",
#             "https://www.googleapis.com/auth/calendar.readonly",
#             "openid",
#         ],
#     )
#     flow.redirect_uri = "http://localhost:8000/users/social-auth-success"

#     authorization_response = request.get_full_path_info()
#     flow.fetch_token(authorization_response=authorization_response)

#     credentials = flow.credentials
#     request.session["credentials"] = {
#         "token": credentials.token,
#         "refresh_token": credentials.refresh_token,
#         "token_uri": credentials.token_uri,
#         "client_id": credentials.client_id,
#         "client_secret": credentials.client_secret,
#         "scopes": credentials.scopes,
#     }
#     return

# def get_django_token(request):
#     credentials = request.session["credentials"]
#     google_token = credentials.token
