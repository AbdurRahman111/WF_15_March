from django.db import models
from datetime import datetime
# Create your models here.

# for making password hash



class Event_Model(models.Model):
    class Meta:
        verbose_name_plural = 'Event'

    Home_Team = models.CharField(max_length=256, blank=True, null=True)
    Way_Team = models.CharField(max_length=256, blank=True, null=True)
    Stadium_Name = models.CharField(max_length=256, blank=True, null=True)
    Event_Logo = models.ImageField(upload_to="event_image/", blank=True, null=True)

    is_game_finished = models.CharField(max_length=256, blank=True, null=True)

    Event_Date_Time = models.DateTimeField(blank=True, null=True)


