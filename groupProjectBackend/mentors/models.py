from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class MentorProfile(models.Model):
    class MentorType(models.TextChoices):
        LEAD = "Lead"
        INDUSTRY = "Industry"
        JUNIOR = "Junior"
        VOLUNTEER = "Volunteer"

    mentor_name = models.CharField(max_length=200)
    mentor_email = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    location = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    mentor_type = models.CharField(max_length=15, choices=MentorType.choices)
    one_day_workshop = models.BooleanField()


class MentorProcess(models.Model):
    mentor_name = models.ForeignKey(
        MentorProfile, related_name="process", on_delete=models.CASCADE
    )
    interview = models.BooleanField(default=False)
    interview_completed = models.DateTimeField(null=True, blank=True)
    offer_position = models.BooleanField(default=False)
    offer_position_completed = models.DateTimeField(null=True, blank=True)
    send_contract = models.BooleanField(default=False)
    send_contract_completed = models.DateTimeField(null=True, blank=True)
    signed_contract = models.BooleanField(default=False)
    signed_contract_completed = models.DateTimeField(null=True, blank=True)
    calendar_invites = models.BooleanField(default=False)
    calendar_invites_completed = models.DateTimeField(null=True, blank=True)
    onboarding = models.BooleanField(default=False)
    onboarding_completed = models.DateTimeField(null=True, blank=True)
    feedback = models.BooleanField(default=False)
    feedback_completed = models.DateTimeField(null=True, blank=True)
    offboarding = models.BooleanField(default=False)
    offboarding_completed = models.DateTimeField(null=True, blank=True)


@receiver(post_save, sender=MentorProfile)
def create_related_process(sender, instance, created, *args, **kwargs):
    if instance and created:
        MentorProcess.objects.create(mentor_name=instance)