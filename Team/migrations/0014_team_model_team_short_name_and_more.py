# Generated by Django 4.1.3 on 2023-03-15 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0013_alter_team_model_team_form_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_model',
            name='Team_short_Name',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='team_model',
            name='Team_Form_Date_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 15, 20, 58, 13, 516919)),
        ),
    ]
