# Generated by Django 3.0.8 on 2020-10-31 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorprocess',
            name='calendar_invites',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mentorprocess',
            name='feedback',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mentorprocess',
            name='interview',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mentorprocess',
            name='offboarding',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mentorprocess',
            name='offer_position',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mentorprocess',
            name='onboarding',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mentorprocess',
            name='send_contract',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mentorprocess',
            name='signed_contract',
            field=models.BooleanField(default=False),
        ),
    ]