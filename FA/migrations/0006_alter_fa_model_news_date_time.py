# Generated by Django 4.1.7 on 2023-03-13 05:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FA', '0005_alter_fa_model_news_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fa_model',
            name='News_Date_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 13, 5, 37, 40, 492670)),
        ),
    ]
