# Generated by Django 4.1.7 on 2023-03-13 05:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goal', '0003_alter_goal_model_goal_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal_model',
            name='Goal_Date_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 13, 5, 24, 29, 586689)),
        ),
    ]
