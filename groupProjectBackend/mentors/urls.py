from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("process/", views.MentorProcessList.as_view()),
    path("process/<int:pk>/", views.MentorProcessDetail.as_view()),
    path("mentor_profile/", views.MentorProfileList.as_view()),
    path("mentor_profile/<int:pk>/", views.MentorProfileDetail.as_view()),
    path("mentor_file_upload/", views.MentorFileUpload.as_view()),
    path("mentor_profile/<str:slug>/", views.MentorTypeList.as_view()),
    path("mentor_skills/<str:slug>/", views.MentorSkillsList.as_view()),
    path("mentor_location/<str:slug>/", views.MentorLocationList.as_view()),
    path("mentor_type/<str:slug>/", views.MentorTypeList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
