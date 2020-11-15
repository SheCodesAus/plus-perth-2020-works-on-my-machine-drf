from googleapiclient.discovery import build
import google.oauth2.credentials
import datetime
from dateutil.relativedelta import *
from .models import Event, Attendance
from mentors.models import MentorProfile
from users.models import CustomUser
import re
import json


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


def find_event_type(name):
    if "Plus" in name:
        event_type = "Plus"
    elif "Flash" in name:
        event_type = "Flash"
    elif "Workshop" in name:
        event_type = "One Day Workshop"
    else:
        event_type = None
    return event_type


def create_event_model(event):
    start = event["start"].get("dateTime", event["start"].get("date"))
    end = event["end"].get("dateTime", event["end"].get("date"))
    name = event["summary"]
    event_type = find_event_type(name)
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
            "event_type": event_type,
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
    email = mentor.get("email")
    try:
        mentor_obj = MentorProfile.objects.get(mentor_email=email)
    except MentorProfile.DoesNotExist:
        mentor_obj = None
    if mentor_obj is not None:
        event_obj = Event.objects.get(pk=event_id)
        attendance = mentor.get("responseStatus")

        attendance_model, created = Attendance.objects.update_or_create(
            event=event_obj,
            mentor=mentor_obj,
            defaults={
                "status": attendance,
            },
        )


def get_calendar_events(credentials):
    creds = json.loads(credentials)
    credentials = google.oauth2.credentials.Credentials.from_authorized_user_info(creds)
    calendar = build("calendar", "v3", credentials=credentials)

    # Get current datetime
    now = datetime.datetime.utcnow()
    # Change date to be 3 months in the past so old events are fetched
    startDate = now + relativedelta(months=-3)
    # Convert to correct format
    startDate = startDate.isoformat() + "Z" # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    events_result = (
        calendar.events()
        .list(
            calendarId="primary",
            timeMin=startDate,
            maxResults=100,
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
        if "She Codes" in event["summary"]:
            event_models.append(create_event_model(event))
        else:
            print("not she codes event")

    return event_models


def create_event(credentials, data):
    print(data)
    creds_string = credentials
    creds_json = json.loads(creds_string)
    creds_obj = google.oauth2.credentials.Credentials.from_authorized_user_info(
        creds_json
    )
    mentors = []

    if len(data["mentor_list"]) > 0:
        for mentor in data["mentor_list"]:
            try:
                mentor_object = MentorProfile.objects.get(mentor_name=mentor)
            except MentorProfile.DoesNotExist:
                mentor_object = None
            if mentor_object is not None:
                mentor_obj = MentorProfile.objects.get(mentor_name=mentor)
                mentor_email = mentor_obj.mentor_email
                mentors.append({"email": mentor_email})

    start = datetime.datetime.strptime(data["event_start"], "%Y-%m-%dT%H:%M")
    start_iso = start.isoformat() + "Z"
    end = datetime.datetime.strptime(data["event_end"], "%Y-%m-%dT%H:%M")
    end_iso = end.isoformat() + "Z"

    event = {
        "summary": data["event_name"],
        "start": {"dateTime": start_iso, "timeZone": "Australia/Perth"},
        "end": {"dateTime": end_iso, "timeZone": "Australia/Perth"},
        "location": data["event_location"],
        "attendees": mentors,
    }
    print(event)
    calendar = build("calendar", "v3", credentials=creds_obj)
    event = (
        calendar.events()
        .insert(calendarId="primary", body=event, sendUpdates="all")
        .execute()
    )
    return get_calendar_events(creds_string)


def update_event(credentials, data, eventId):
    creds = json.loads(credentials)
    credentials = google.oauth2.credentials.Credentials.from_authorized_user_info(creds)

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

    # for mentor_status in data["attendance_set"]:
    #     # breakpoint()
    #     mentor_obj = MentorProfile.objects.get(mentor_name=mentor_status["mentor"])
    #     mentor_email = mentor_obj.mentor_email
    #     mentor_status["mentor"] = mentor_email

    updated_event = (
        calendar.events()
        .update(calendarId="primary", eventId=event["id"], body=event)
        .execute()
    )

    return create_event_model(event)


def delete_event(credentials, eventId):
    creds = json.loads(credentials)
    credentials = google.oauth2.credentials.Credentials.from_authorized_user_info(creds)

    calendar = build("calendar", "v3", credentials=credentials)
    calendar.events().delete(calendarId="primary", eventId=eventId).execute()

    return