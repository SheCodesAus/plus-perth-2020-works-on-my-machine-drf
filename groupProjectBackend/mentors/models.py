from django.db import models

class MentorProfile(models.Model):
    mentor_name = models.CharField(max_length=200)
    mentor_email = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    location = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    mentor_type = models.CharField(max_length=200)
    one_day_workshop = models.BooleanField()

class MentorProcess(models.Model):
    mentor_name = models.ForeignKey(
        MentorProfile, related_name='mentor', on_delete=models.CASCADE)
    step_one = models.BooleanField()
    step_two = models.BooleanField()
    step_three = models.BooleanField()
    step_four = models.BooleanField()
    step_five = models.BooleanField()
    step_six = models.BooleanField()
    step_seven = models.BooleanField()
    step_eight = models.BooleanField()