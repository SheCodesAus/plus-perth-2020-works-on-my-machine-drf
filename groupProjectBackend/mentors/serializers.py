from rest_framework import serializers
from .models import MentorProfile, MentorProcess

class MentorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfile
        fields = ['id', 
        'mentor_name', 
        'mentor_email', 
        'phone_number', 
        'location', 
        'skills', 
        'mentor_type', 
        'one_day_workshop'
        ]
    
    def update(self, instance, validated_data):
        instance.mentor_name = validated_data.get('mentor_name', instance.mentor_name)
        instance.mentor_email = validated_data.get('mentor_email', instance.mentor_email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.location = validated_data.get('location', instance.location)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.mentor_type = validated_data.get('mentor_type', instance.mentor_type)
        instance.one_day_workshop = validated_data.get('one_day_workshop', instance.one_day_workshop)

    def delete(self, validated_data):
        return MentorProfile.objects.delete(**validated_data)


class MentorProcessSerializer(serializers.ModelSerializer):
    mentor = MentorProfileSerializer(read_only=True)
    
    class Meta:
            model = MentorProcess
            fields = ['id', 
            'mentor',
            'interview',
            'offer_position',
            'send_contract',
            'signed_contract',
            'calendar_invites',
            'onboarding',
            'feedback',
            'offboarding'
            'interview_created',
            'offer_position_created',
            'send_contract_created',
            'signed_contract_created',
            'calendar_invites_created',
            'onboarding_created',
            'feedback_created',
            'offboarding_created'
            ] 
    
    def update(self, instance, validated_data):
        instance.interview = validated_data.get('interview', instance.interview)
        instance.interview_created = validated_data.get('interview_created', instance.interview)
        instance.offer_position = validated_data.get('offer_position', instance.offer_position)
        instance.offer_position_created = validated_data.get('offer_position_created', instance.offer_position)
        instance.send_contract = validated_data.get('send_contract', instance.send_contract)
        instance.send_contract_created = validated_data.get('send_contract', instance.send_contract)
        instance.signed_contract = validated_data.get('signed_contract', instance.signed_contract)
        instance.signed_contract_created = validated_data.get('signed_contract', instance.signed_contract)
        instance.calendar_invites = validated_data.get('calendar_invites', instance.calendar_invites)
        instance.calendar_invites_created = validated_data.get('calendar_invites', instance.calendar_invites)
        instance.onboarding = validated_data.get('onboarding', instance.onboarding)
        instance.onboarding_created = validated_data.get('onboarding', instance.onboarding)
        instance.feedback = validated_data.get('feedback', instance.feedback)
        instance.offboarding_created = validated_data.get('offboarding', instance.offboarding)

    def delete(self, validated_data):
        return MentorProcess.objects.delete(**validated_data)
   
    
    