from ics import Calendar
import requests
import datetime
from .models import Event
from mentors.models import MentorProfile
from users.models import CustomUser


def get_events(url):
    cal = Calendar(requests.get(url).text)
    now = datetime.date.today()
    events = []

    for event in cal.events:
        creator_email = event.organizer.email
        creator = CustomUser.objects.get(email=creator_email)
        start_date = event.begin.date()
        start = event.begin.datetime
        end = event.end.datetime
        all_day = event.all_day

        if start_date > now:
            mentors = []
            for mentor in event.attendees:

                mentor_email = mentor.email
                mentor_obj = MentorProfile.objects.get(mentor_email=mentor_email)
                mentor_id = mentor_obj.pk
                mentors.append(mentor_id)
            event, created = Event.objects.update_or_create(
                id=event.uid,
                defaults={
                    "creator": creator,
                    "event_start": start,
                    "event_end": end,
                    "event_name": event.name,
                    "event_location": event.location,
                    "all_day": event.all_day,
                },
            )
            event.mentor_list.set(mentors)
            event.save()
            events.append(event)
    return events