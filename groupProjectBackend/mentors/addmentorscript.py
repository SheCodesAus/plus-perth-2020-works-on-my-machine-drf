from .models import MentorProfile


def create_new_mentor(mentors):
    for mentor in mentors:
        if mentor["workshop"] == "TRUE":
            workshop = True
        else:
            workshop = False
        mentor_data, created = MentorProfile.objects.update_or_create(
            mentor_name=mentor["name"],
            defaults={
                "mentor_email": mentor["email"],
                "phone_number": mentor["phone"],
                "location": mentor["location"],
                "skills": mentor["skills"],
                "mentor_type": mentor["position"],
                "one_day_workshop": workshop,
            },
        )
    return mentors