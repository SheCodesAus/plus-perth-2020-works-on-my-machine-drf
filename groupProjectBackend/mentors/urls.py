from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
path('', views.MentorProfileList.as_view()),
path('mentor_process/', views.MentorProcessList.as_view()),
path('mentor_process_detail/<int:pk>/', views.MentorProcessDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)