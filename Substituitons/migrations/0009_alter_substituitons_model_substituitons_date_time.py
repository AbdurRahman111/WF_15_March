# Generated by Django 4.1.7 on 2023-03-13 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Substituitons', '0008_alter_substituitons_model_substituitons_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='substituitons_model',
            name='Substituitons_Date_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 13, 5, 42, 7, 884493)),
        ),
    ]
