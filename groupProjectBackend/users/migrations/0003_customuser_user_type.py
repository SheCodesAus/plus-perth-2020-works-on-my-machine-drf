# Generated by Django 3.0.8 on 2020-10-24 02:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
