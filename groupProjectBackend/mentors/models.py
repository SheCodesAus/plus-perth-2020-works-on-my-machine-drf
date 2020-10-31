from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
        MentorProfile, related_name="mentor", on_delete=models.CASCADE
    )
    interview = models.BooleanField(default=False)
    offer_position = models.BooleanField(default=False)
    send_contract = models.BooleanField(default=False)
    signed_contract = models.BooleanField(default=False)
    calendar_invites = models.BooleanField(default=False)
    onboarding = models.BooleanField(default=False)
    feedback = models.BooleanField(default=False)
    offboarding = models.BooleanField(default=False)


@receiver(post_save, sender=MentorProfile)
def create_related_process(sender, instance, created, *args, **kwargs):
    if instance and created:
        MentorProcess.objects.create(mentor_name=instance)