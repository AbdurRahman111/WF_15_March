# Generated by Django 4.1.7 on 2023-03-13 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FA', '0011_alter_fa_model_news_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fa_model',
            name='News_Date_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 13, 9, 53, 11, 666913)),
        ),
    ]
