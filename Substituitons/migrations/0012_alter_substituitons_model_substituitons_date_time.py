# Generated by Django 4.1.7 on 2023-03-13 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Substituitons', '0011_alter_substituitons_model_substituitons_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='substituitons_model',
            name='Substituitons_Date_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 13, 9, 53, 11, 664130)),
        ),
    ]
