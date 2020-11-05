from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path("events/", views.EventList.as_view()),
    path("events/<str:pk>/", views.EventDetail.as_view()),
    path("create-event/", views.CreateEvent.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)