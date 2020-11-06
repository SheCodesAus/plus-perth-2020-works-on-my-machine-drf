from .models import MentorProfile


def create_new_mentor():
    mentors = [
        {
            "date": "22/05/2020 2:43:54",
            "email": "test1@shecodes.com.au",
            "name": "Jess Budd",
            "phone": "400000001",
            "mentor_type": "Industry",
            "skills": "HTML/CSS",
            "location": "Perth",
        },
        {
            "date": "22/05/2020 2:43:54",
            "email": "test2@shecodes.com.au",
            "name": "Ben Durham",
            "phone": "400000002",
            "mentor_type": "Industry",
            "skills": "Javascript and React",
            "location": "Perth",
        },
        {
            "date": "22/05/2020 2:43:54",
            "email": "test3@shecodes.com.au",
            "name": "Amy",
            "phone": "400000003",
            "mentor_type": "Industry",
            "skills": "HTML/CSS, Javascript and React",
            "location": "Perth",
        },
        {
            "date": "22/05/2020 2:43:54",
            "email": "test4@shecodes.com.au",
            "name": "Somayra Mamsa",
            "phone": "400000004",
            "mentor_type": "Junior",
            "skills": "HTML/CSS",
            "location": "Perth",
        },
        {
            "date": "22/05/2020 2:43:54",
            "email": "test5@shecodes.com.au",
            "name": "Alexander Karan",
            "phone": "400000005",
            "mentor_type": "Industry",
            "skills": "HTML/CSS, Python, Javascript and React",
            "location": "Perth",
        },
        {
            "date": "22/05/2020 2:43:54",
            "email": "test6@shecodes.com.au",
            "name": "Rami Ruhayel",
            "phone": "400000006",
            "mentor_type": "Industry",
            "skills": "HTML/CSS, Python",
            "location": "Perth",
        },
    ]

    for mentor in mentors:
        mentor_data, created = MentorProfile.objects.update_or_create(
            mentor_name=mentor["name"],
            defaults={
                "mentor_email": mentor["email"],
                "phone_number": mentor["phone"],
                "location": mentor["location"],
                "skills": mentor["skills"],
                "mentor_type": mentor["mentor_type"],
                "one_day_workshop": False,
            },
        )
    return mentors