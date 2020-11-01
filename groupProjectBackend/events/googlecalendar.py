from googleapiclient.discovery import build
import google.oauth2.credentials
import datetime
from .models import Event
from mentors.models import MentorProfile
from users.models import CustomUser


def create_event_model(event):
    start = event["start"].get("dateTime", event["start"].get("date"))
    end = event["end"].get("dateTime", event["end"].get("date"))
    name = event["summary"]
    location = event.get("location")
    event_id = event.get("id")
    creator_email = event["creator"].get("email")
    mentors = []

    if "attendees" in event:
        for mentor in event["attendees"]:
            mentor_email = mentor.get("email")
            mentor_obj = MentorProfile.objects.get(mentor_email=mentor_email)
            mentor_id = mentor_obj.pk
            mentors.append(mentor_obj)

    print(creator_email, start, end, name, location, mentors)

    event_model, created = Event.objects.update_or_create(
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
    event_model.mentor_list.set(mentors)
    event_model.save()
    return event_model


def get_calendar_events(credentials):
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
    event_list = []

    if not events:
        print("No upcoming events found.")
        return []

    event_models = []
    for event in events:
        event_models.append(create_event_model(event))

    return event_models


def create_event(credentials, data):
    creds = google.oauth2.credentials.Credentials(**credentials)
    mentors = []

    for mentor in data["mentor_list"]:
        mentor_obj = MentorProfile.objects.get(pk=mentor)
        # breakpoint()
        mentor_email = mentor_obj.mentor_email
        mentors.append({"email": mentor_email})
        # breakpoint()

    event = {
        "summary": data["event_name"],
        "start": {"dateTime": data["event_start"], "timeZone": "Australia/Perth"},
        "end": {"dateTime": data["event_end"], "timeZone": "Australia/Perth"},
        "location": data["event_location"],
        "attendees": mentors,
    }
    print(event)

    calendar = build("calendar", "v3", credentials=creds)
    event = (
        calendar.events()
        .insert(calendarId="primary", body=event, sendUpdates="all")
        .execute()
    )

    return get_calendar_events(credentials)