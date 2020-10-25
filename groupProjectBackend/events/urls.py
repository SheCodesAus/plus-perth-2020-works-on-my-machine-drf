from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('calendar-url/', views.AddCalendar.as_view()),
    path('events/', views.Events.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)