from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('calendar-url/', views.AddCalendar.as_view()),
    path('events/', views.EventList.as_view()),
    path('events/<str:pk>/', views.EventDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)