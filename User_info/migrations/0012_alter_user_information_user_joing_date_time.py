# Generated by Django 4.1.7 on 2023-03-13 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_info', '0011_alter_user_information_user_joing_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_information',
            name='User_Joing_Date_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 13, 5, 43, 31, 125852)),
        ),
    ]
