from django.db import models
from datetime import datetime
# Create your models here.

from Event.models import Event_Model
from Team.models import Team_Model




# goal and substitution are connect from event
class Game_Model(models.Model):
    class Meta:
        verbose_name_plural = 'Game'

    Event_for_game = models.ForeignKey(Event_Model, on_delete=models.CASCADE, blank=True, null=True)
    # Team_for_game = models.ForeignKey(Team_Model, on_delete=models.CASCADE, blank=True, null=True)

    Home_Team_Score = models.IntegerField(default=0)
    Way_Team_Score = models.IntegerField(default=0)
    Win_or_Lose_team_auto = models.CharField(max_length=256, blank=True, null=True)

    Home_Team_Shot_on_target = models.CharField(max_length=256, blank=True, null=True)
    Way_Team_Shot_on_target = models.CharField(max_length=256, blank=True, null=True)
    Home_Team_Position = models.CharField(max_length=256, blank=True, null=True)
    Way_Team_Position = models.CharField(max_length=256, blank=True, null=True)
    Home_Team_Corner = models.CharField(max_length=256, blank=True, null=True)
    Way_Team_Corner = models.CharField(max_length=256, blank=True, null=True)





    # record for home team
    home_Team_name  = models.CharField(max_length=256, blank=True, null=True)
    home_Team_manager_name  = models.CharField(max_length=256, blank=True, null=True)

    home_Team_player_1_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_2_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_3_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_4_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_5_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_6_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_7_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_8_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_9_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_10_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_11_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_12_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_13_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_14_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_15_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_16_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_17_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_18_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)

    home_Team_player_active_1_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_active_2_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_active_3_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_active_4_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_active_5_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_active_6_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_active_7_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_active_8_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_active_9_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_active_10_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_active_11_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)

    home_Team_player_substitute_1_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_substitute_2_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_substitute_3_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_substitute_4_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_substitute_5_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_substitute_6_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    home_Team_player_substitute_7_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    # ----------------------------------------------------------------------------------------------------



    # record for way team
    way_Team_name = models.CharField(max_length=256, blank=True, null=True)
    way_Team_manager_name = models.CharField(max_length=256, blank=True, null=True)

    way_Team_player_1_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_2_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_3_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_4_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_5_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_6_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_7_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_8_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_9_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_10_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_11_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_12_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_13_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_14_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_15_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_16_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_17_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_18_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)

    way_Team_player_active_1_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_active_2_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_active_3_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_active_4_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_active_5_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_active_6_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_active_7_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_active_8_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_active_9_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_active_10_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_active_11_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)

    way_Team_player_substitute_1_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_substitute_2_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_substitute_3_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_substitute_4_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_substitute_5_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_substitute_6_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    way_Team_player_substitute_7_id_from_Plyer_model = models.CharField(max_length=256, blank=True, null=True)
    # -------------------------------------------------------------------------------------------------------

    is_game_finished = models.CharField(max_length=256, blank=True, null=True)

    live_game_link = models.CharField(max_length=256, blank=True, null=True)

    Game_Date_Time = models.DateTimeField(default=datetime.now(), blank=True)



