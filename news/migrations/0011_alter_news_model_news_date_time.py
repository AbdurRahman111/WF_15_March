# Generated by Django 4.1.7 on 2023-03-13 05:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_alter_news_model_news_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_model',
            name='News_Date_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 13, 5, 43, 31, 133425)),
        ),
    ]
