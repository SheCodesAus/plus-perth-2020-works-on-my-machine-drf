from django.db import models
from django.contrib.auth import get_user_model


class Event(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=200)
    creator = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="event"
    )
    event_city = models.CharField(max_length=200)
    event_name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200)
    event_start = models.DateTimeField(max_length=200)
    event_end = models.DateTimeField(max_length=200)
    event_location = models.CharField(max_length=200, null=True, blank=True)
    all_day = models.BooleanField(default=False)
    mentor_list = models.ManyToManyField(
        "mentors.MentorProfile",
        related_name="event_attending",
        related_query_name="mentor_attending",
    )


class CalendarUrl(models.Model):
    calendar_url = models.URLField()
