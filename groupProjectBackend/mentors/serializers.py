from rest_framework import serializers
from .models import MentorProfile, MentorProcess


class MentorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfile
        fields = [
            "id",
            "mentor_name",
            "mentor_email",
            "phone_number",
            "location",
            "skills",
            "mentor_type",
            "one_day_workshop",
        ]

    def create(self, validated_data):
        return MentorProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.mentor_name = validated_data.get("mentor_name", instance.mentor_name)
        instance.mentor_email = validated_data.get(
            "mentor_email", instance.mentor_email
        )
        instance.phone_number = validated_data.get(
            "phone_number", instance.phone_number
        )
        instance.location = validated_data.get("location", instance.location)
        instance.skills = validated_data.get("skills", instance.skills)
        instance.mentor_type = validated_data.get("mentor_type", instance.mentor_type)
        instance.one_day_workshop = validated_data.get(
            "one_day_workshop", instance.one_day_workshop
        )

        instance.save()
        return instance

    def delete(self, validated_data):
        return MentorProfile.objects.delete(**validated_data)


class MentorProcessSerializer(serializers.ModelSerializer):
    mentor = MentorProfileSerializer(read_only=True)

    class Meta:
        model = MentorProcess
        fields = [
            "id",
            "mentor",
            "interview",
            "interview_completed",
            "offer_position",
            "offer_position_completed",
            "send_contract",
            "send_contract_completed",
            "signed_contract",
            "signed_contract_completed",
            "calendar_invites",
            "calendar_invites_completed",
            "onboarding",
            "onboarding_completed",
            "feedback",
            "feedback_completed",
            "offboarding",
            "offboarding_completed",
        ]

    def update(self, instance, validated_data):
        instance.interview = validated_data.get("interview", instance.interview)
        instance.interview_completed = validated_data.get(
            "interview_completed", instance.interview_completed
        )

        instance.offer_position = validated_data.get(
            "offer_position", instance.offer_position
        )
        instance.offer_position_completed = validated_data.get(
            "offer_position_completed", instance.offer_position_completed
        )

        instance.send_contract = validated_data.get(
            "send_contract", instance.send_contract
        )
        instance.send_contract_completed = validated_data.get(
            "send_contract_completed", instance.send_contract_completed
        )

        instance.signed_contract = validated_data.get(
            "signed_contract", instance.signed_contract
        )
        instance.signed_contract_completed = validated_data.get(
            "signed_contract_completed", instance.signed_contract_completed
        )

        instance.calendar_invites = validated_data.get(
            "calendar_invites", instance.calendar_invites
        )
        instance.calendar_invites_completed = validated_data.get(
            "calendar_invites_completed", instance.calendar_invites_completed
        )

        instance.onboarding = validated_data.get("onboarding", instance.onboarding)
        instance.onboarding_completed = validated_data.get(
            "onboarding_completed", instance.onboarding_completed
        )

        instance.feedback = validated_data.get("feedback", instance.feedback)
        instance.feedback_completed = validated_data.get(
            "feedback_completed", instance.feedback_completed
        )

        instance.offboarding = validated_data.get("offboarding", instance.offboarding)
        instance.offboarding_completed = validated_data.get(
            "offboarding_completed", instance.offboarding_completed
        )
        instance.save()
        return instance

    def delete(self, validated_data):
        return MentorProcess.objects.delete(**validated_data)
