from django.db import models
from datetime import datetime
# Create your models here.

from Event.models import Event_Model


class Goal_Model(models.Model):
    class Meta:
        verbose_name_plural = 'Goal'

    Event_for_goal = models.ForeignKey(Event_Model, on_delete=models.CASCADE, related_name="event_here", blank=True, null=True)

    Home_Team_Goal_Count_In_1 = models.CharField(max_length=256, blank=True, null=True)
    Way_Team_Goal_Count_In_1 = models.CharField(max_length=256, blank=True, null=True)
    Scorer_Name = models.CharField(max_length=256, blank=True, null=True)
    Goal_Assist_Name = models.CharField(max_length=256, blank=True, null=True)

    Goal_Date_Time = models.DateTimeField(default=datetime.now(), blank=True)

    # @property
    # def event_name(self):
    #     return self.Event_Model.Home_Team



