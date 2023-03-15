from django.db import models
from datetime import datetime
# Create your models here.

from Event.models import Event_Model


class Substituitons_Model(models.Model):
    class Meta:
        verbose_name_plural = 'Substituitons'

    Event_for_goal = models.ForeignKey(Event_Model, on_delete=models.CASCADE, related_name="event_Substituitons_here", blank=True, null=True)

    PLayer_Name = models.CharField(max_length=256, blank=True, null=True)
    Substituitons_Name = models.CharField(max_length=256, blank=True, null=True)
    substitute_team_Home_or_way = models.CharField(max_length=256, blank=True, null=True)


    Substituitons_Date_Time = models.DateTimeField(default=datetime.now(), blank=True)



