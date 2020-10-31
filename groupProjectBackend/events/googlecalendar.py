from googleapiclient.discovery import build
import google.oauth2.credentials
import datetime
from .models import Event
from mentors.models import MentorProfile
from users.models import CustomUser


def getCalendarEvents(credentials):
    credentials = google.oauth2.credentials.Credentials(**credentials)

    calendar = build("calendar", "v3", credentials=credentials)
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time

    print("Getting the upcoming 10 events")
    events_result = (
        calendar.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
        print("No upcoming events found.")
    for event in events:
        creator_email = event["creator"].get("email")
        start = event["start"].get("dateTime", event["start"].get("date"))
        end = event["end"].get("dateTime", event["end"].get("date"))
        name = event["summary"]
        location = event.get("location")
        event_id = event.get("id")
        mentors = []

        if "attendees" in event:
            for mentor in event["attendees"]:
                mentor_email = mentor.get("email")
                mentor_obj = MentorProfile.objects.get(mentor_email=mentor_email)
                mentor_id = mentor_obj.pk
                mentors.append(mentor_id)

        print(creator_email, start, end, name, location, mentors)

        event, created = Event.objects.update_or_create(
            id=event_id,
            defaults={
                "creator": CustomUser.objects.get(email=creator_email),
                "event_start": start,
                "event_end": end,
                "event_name": name,
                "event_location": location,
                "all_day": False,
            },
        )
        event.mentor_list.set(mentors)
        event.save()
        events.append(event)
    return events


def createEvent(credentials, data):
    credentials = google.oauth2.credentials.Credentials(**credentials)

    mentors = []

    for mentor in data.mentor_list:
        mentor_obj = MentorProfile.objects.get(pk=mentor)
        mentor_email = mentor_obj.email
        mentors.append(mentor_email)

    event = {
        "summary": data.name,
        "start": {"dateTime": data.event_start, "timeZone": "Australia/Perth"},
        "end": {"dateTime": data.event_end, "timeZone": "Australia/Perth"},
        "location": data.event_location,
        "attendees": mentors,
    }

    calendar = build("calendar", "v3", credentials=credentials)
    event = service.events().insert(calendarId="primary", body=event).execute()