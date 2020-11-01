from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view(), name="users"),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
    path('users/social-auth', views.SocialAuth.as_view()),
    path('users/social-auth-success', views.SocialAuthSuccess.as_view(), name="auth-success"),
]

urlpatterns = format_suffix_patterns(urlpatterns)