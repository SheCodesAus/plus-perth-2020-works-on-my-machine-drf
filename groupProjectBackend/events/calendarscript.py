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
        creator_id = creator.pk
        start = event.begin.date()
        end = event.end.date()

        if start > now:
            event, created = Event.objects.get_or_create(
                id=event.uid,
                creator = creator_id,
                event_start=start,
                event_end=end,
                event_name=event.name,
            )
            events.append(event)
    return events