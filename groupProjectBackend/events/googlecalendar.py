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

    # if not events:
    #     print("No upcoming events found.")
    # for event in events:
    #     start = event["start"].get("dateTime", event["start"].get("date"))
    #     print(start, event["summary"])

    if not events:
        print("No upcoming events found.")
    for event in events:
        creator_email = event["creator"].get("email")
        start = event["start"].get("dateTime", event["start"].get("date"))
        end = event["end"].get("dateTime", event["end"].get("date"))
        name = event["summary"]
        location = event.get("location")
        # mentors = []

        # for mentor in event["attendees"]:
        #     mentor_email = mentor.get("email")
        #     mentor_obj = MentorProfile.objects.get(mentor_email=mentor_email)
        #     mentor_id = mentor_obj.pk
        #     mentors.append(mentor_id)

        print(creator_email, start, end, name, location)
