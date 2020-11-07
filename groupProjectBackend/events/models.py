from django.db import models
from django.contrib.auth import get_user_model


class Event(models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=200)
    creator = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="event"
    )
    event_city = models.CharField(max_length=200, null=True, blank=True)
    event_name = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200, null=True, blank=True)
    event_start = models.DateTimeField(max_length=200)
    event_end = models.DateTimeField(max_length=200)
    event_location = models.CharField(max_length=200, null=True, blank=True)
    all_day = models.BooleanField(default=False)
    mentor_list = models.ManyToManyField(
        "mentors.MentorProfile",
        through="Attendance",
        through_fields=("event", "mentor"),
    )


class Attendance(models.Model):
    class Status(models.TextChoices):
        N = "needsAction", "Needs Action"
        D = "declined", "Declined"
        T = "tentative", "Tentative"
        A = "accepted", "Accepted"

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.N, null=True
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    mentor = models.ForeignKey(
        "mentors.MentorProfile",
        on_delete=models.CASCADE,
    )