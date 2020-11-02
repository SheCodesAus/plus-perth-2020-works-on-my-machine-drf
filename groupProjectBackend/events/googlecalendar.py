from googleapiclient.discovery import build
import google.oauth2.credentials
import datetime
from .models import Event, Attendance
from mentors.models import MentorProfile
from users.models import CustomUser
import re


def find_event_city(location):
    if location is not None:
        postcode = re.findall("(6|3)[0-9]{3}", location)
        if postcode[0] == "6":
            return "Perth"
        elif postcode[0] == "4":
            return "Brisbane"
        else:
            return None
    else:
        return None


def create_event_model(event):
    start = event["start"].get("dateTime", event["start"].get("date"))
    end = event["end"].get("dateTime", event["end"].get("date"))
    name = event["summary"]
    location = event.get("location")
    city = find_event_city(location)
    event_id = event.get("id")
    creator_email = event["creator"].get("email")

    event_model, created = Event.objects.update_or_create(
        id=event_id,
        defaults={
            "creator": CustomUser.objects.get(email=creator_email),
            "event_start": start,
            "event_end": end,
            "event_name": name,
            "event_location": location,
            "event_city": city,
            "all_day": False,
        },
    )

    if "attendees" in event:
        for mentor in event["attendees"]:
            create_attendance_model(mentor, event_id)

    return event_model


def create_attendance_model(mentor, event_id):
    event_obj = Event.objects.get(pk=event_id)
    mentor_email = mentor.get("email")
    mentor_obj = MentorProfile.objects.get(mentor_email=mentor_email)
    attendance = mentor.get("responseStatus")

    # breakpoint()
    attendance_model, created = Attendance.objects.update_or_create(
        event=event_obj,
        mentor=mentor_obj,
        defaults={
            "status": attendance,
        },
    )


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
    print(events)
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
        mentor_email = mentor_obj.mentor_email
        mentors.append({"email": mentor_email})

    event = {
        "summary": data["event_name"],
        "start": {"dateTime": data["event_start"], "timeZone": "Australia/Perth"},
        "end": {"dateTime": data["event_end"], "timeZone": "Australia/Perth"},
        "location": data["event_location"],
        "attendees": mentors,
    }

    calendar = build("calendar", "v3", credentials=creds)
    event = (
        calendar.events()
        .insert(calendarId="primary", body=event, sendUpdates="all")
        .execute()
    )

    return get_calendar_events(credentials)


def update_event(credentials, data, eventId):
    credentials = google.oauth2.credentials.Credentials(**credentials)

    calendar = build("calendar", "v3", credentials=credentials)
    event = calendar.events().get(calendarId="primary", eventId=eventId).execute()

    if "event_name" in data:
        event["summary"] = data["event_name"]

    if "event_start" in data:
        event["start"] = {
            "dateTime": data["event_start"],
            "timeZone": "Australia/Perth",
        }

    if "event_end" in data:
        event["end"] = {"dateTime": data["event_end"], "timeZone": "Australia/Perth"}

    if "event_location" in data:
        event["location"] = data["event_location"]

    if "mentor_list" in data:
        mentors = []
        for mentor in data["mentor_list"]:
            mentor_obj = MentorProfile.objects.get(pk=mentor)
            mentor_email = mentor_obj.mentor_email
            mentors.append({"email": mentor_email})
        event["attendees"] = mentors
    updated_event = (
        calendar.events()
        .update(calendarId="primary", eventId=event["id"], body=event)
        .execute()
    )

    return create_event_model(event)


def delete_event(credentials, eventId):
    creds = google.oauth2.credentials.Credentials(**credentials)
    calendar = build("calendar", "v3", credentials=creds)
    calendar.events().delete(calendarId="primary", eventId=eventId).execute()

    return