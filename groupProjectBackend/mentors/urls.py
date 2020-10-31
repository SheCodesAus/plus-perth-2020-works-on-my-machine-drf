from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
path('process/', views.MentorProcessList.as_view()),
path('process/<int:pk>/', views.MentorProcessDetail.as_view()),
path('mentor_profile/', views.MentorProfileList.as_view()),
path('mentor_profile/<int:pk>/', views.MentorProfileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)