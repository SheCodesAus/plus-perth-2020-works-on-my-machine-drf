# Generated by Django 3.0.8 on 2020-10-31 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0002_auto_20201031_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentorprocess',
            name='mentor_name',
        ),
        migrations.AddField(
            model_name='mentorprocess',
            name='mentor',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='process', to='mentors.MentorProfile'),
            preserve_default=False,
        ),
    ]