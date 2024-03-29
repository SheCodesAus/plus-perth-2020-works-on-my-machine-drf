# Generated by Django 3.0.8 on 2020-11-12 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('needsAction', 'Needs Action'), ('declined', 'Declined'), ('tentative', 'Tentative'), ('accepted', 'Accepted')], default='needsAction', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('event_city', models.CharField(blank=True, max_length=200, null=True)),
                ('event_name', models.CharField(max_length=200)),
                ('event_type', models.CharField(blank=True, max_length=200, null=True)),
                ('event_start', models.DateTimeField(max_length=200)),
                ('event_end', models.DateTimeField(max_length=200)),
                ('event_location', models.CharField(blank=True, max_length=200, null=True)),
                ('all_day', models.BooleanField(default=False)),
            ],
        ),
    ]
