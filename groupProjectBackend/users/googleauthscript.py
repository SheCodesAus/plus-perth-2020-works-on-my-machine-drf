import google_auth_oauthlib.flow

scopes_list = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/calendar.readonly",
    "openid",
]
client_config = {
    "web": {
        "client_id": "318837040339-j5bjsgdg6n9flpprukrk9foiu3493jvj.apps.googleusercontent.com",
        "project_id": "quickstart-1603938918834",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "iJzQhuApcbNTwwq182ALqCWJ",
        "redirect_uris": [
            "https://shecodes-portal-drf.herokuapp.com/users/social-auth-success",
            "http://localhost:8000/users/social-auth-success",
        ],
        "javascript_origins": [
            "https://shecodes-portal-drf.herokuapp.com",
            "http://localhost:3000",
            "http://localhost:8000",
        ],
    }
}


def set_flow_dev():
    # Use this for testing locally

    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        client_config=client_config, scopes=scopes_list
    )
    flow.redirect_uri = "http://localhost:3000/social-auth-success"
    return flow


def set_flow_prod():
    # Use this for deploying to production

    flow = google_auth_oauthlib.flow.Flow.from_client_config(
        client_config=client_config, scopes=scopes_list
    )
    flow.redirect_uri = (
        "https://shecodes-portal-react.herokuapp.com/social-auth-success"
    )
    return flow