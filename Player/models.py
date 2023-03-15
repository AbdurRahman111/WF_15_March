from django.db import models
from datetime import datetime
# Create your models here.




class Player_Model(models.Model):
    # class Meta:
    #     verbose_name_plural = 'Player'


    PLayer_Name = models.CharField(max_length=256, blank=True, null=True)
    PLayer_Jersey = models.CharField(max_length=256, blank=True, null=True)
    PLayer_Position = models.CharField(max_length=256, blank=True, null=True)
    PLayer_Age = models.CharField(max_length=256, blank=True, null=True)
    Total_goal_count = models.IntegerField(default=0)
    Total_assist_count = models.IntegerField(default=0)

    PLayer_Photo = models.ImageField(upload_to="pLayer_photo/", blank=True, null=True)
    Base_price = models.CharField(max_length=256, blank=True, null=True)
    Sell_price = models.CharField(max_length=256, blank=True, null=True)

    player_local_or_foreign = models.CharField(max_length=256, blank=True, null=True)

    Description = models.TextField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'Player'

    def __str__(self):
        return self.PLayer_Name


