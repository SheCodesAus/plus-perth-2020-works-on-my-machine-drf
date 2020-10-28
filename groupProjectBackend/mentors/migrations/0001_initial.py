# Generated by Django 3.0.8 on 2020-10-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MentorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_name', models.CharField(max_length=200)),
                ('mentor_email', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('mentor_type', models.CharField(max_length=200)),
                ('one_day_workshop', models.BooleanField()),
            ],
        ),
    ]