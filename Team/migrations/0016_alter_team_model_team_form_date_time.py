# Generated by Django 4.1.7 on 2023-03-15 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0015_alter_team_model_team_form_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_model',
            name='Team_Form_Date_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 15, 23, 12, 53, 769092)),
        ),
    ]