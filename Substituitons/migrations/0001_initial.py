# Generated by Django 4.1.7 on 2023-03-13 05:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Substituitons_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PLayer_Name', models.CharField(blank=True, max_length=256, null=True)),
                ('Substituitons_Name', models.CharField(blank=True, max_length=256, null=True)),
                ('substitute_team_Home_or_way', models.CharField(blank=True, max_length=256, null=True)),
                ('Substituitons_Date_Time', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 13, 5, 15, 47, 453477))),
                ('Event_for_goal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_Substituitons_here', to='Event.event_model')),
            ],
            options={
                'verbose_name_plural': 'Substituitons',
            },
        ),
    ]
