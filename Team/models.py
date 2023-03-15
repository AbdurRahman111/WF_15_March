from django.db import models
from datetime import datetime
# Create your models here.
from User_info.models import User_information
from Player.models import Player_Model



class Team_Model(models.Model):
    class Meta:
        verbose_name_plural = 'Team'

    Manager = models.ForeignKey(User_information, on_delete=models.CASCADE, blank=True, null=True)

    Team_player_1_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_1')
    Team_player_2_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_2')
    Team_player_3_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_3')
    Team_player_4_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_4')
    Team_player_5_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_5')
    Team_player_6_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_6')
    Team_player_7_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_7')
    Team_player_8_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_8')
    Team_player_9_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_9')
    Team_player_10_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_10')
    Team_player_11_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_11')
    Team_player_12_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_12')
    Team_player_13_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_13')
    Team_player_14_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_14')
    Team_player_15_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_15')
    Team_player_16_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_16')
    Team_player_17_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_17')
    Team_player_18_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_all_18')

    Team_player_active_1_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_ac_1')
    Team_player_active_2_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_ac_2')
    Team_player_active_3_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_ac_3')
    Team_player_active_4_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_ac_4')
    Team_player_active_5_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_ac_5')
    Team_player_active_6_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_ac_6')
    Team_player_active_7_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_ac_7')
    Team_player_active_8_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_ac_8')
    Team_player_active_9_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_ac_9')
    Team_player_active_10_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_ac_10')
    Team_player_active_11_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_ac_11')

    Team_player_substitute_1_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True,null=True, related_name='topic_content_type_st_1')
    Team_player_substitute_2_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_st_2')
    Team_player_substitute_3_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_st_3')
    Team_player_substitute_4_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_st_4')
    Team_player_substitute_5_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_st_5')
    Team_player_substitute_6_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_st_6')
    Team_player_substitute_7_id_from_Plyer_model = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='topic_content_type_st_7')

    Team_captain = models.ForeignKey(Player_Model, on_delete=models.CASCADE, blank=True, null=True, related_name='Team_captain')

    Team_Name = models.CharField(max_length=256, blank=True, null=True, unique=True)
    Team_short_Name = models.CharField(max_length=256, blank=True, null=True, unique=True)

    Team_Owner_Name = models.CharField(max_length=256, blank=True, null=True)
    Team_Total_play_count = models.IntegerField(default=0)

    Win_count = models.IntegerField(default=0)
    Loos_count = models.IntegerField(default=0)
    Drow_count = models.IntegerField(default=0)
    GF = models.IntegerField(default=0)
    GA = models.IntegerField(default=0)
    GD = models.IntegerField(default=0)
    PTS = models.IntegerField(default=0)

    Team_Official_Link = models.CharField(max_length=256, blank=True, null=True)

    Team_Logo = models.ImageField(blank=True, null=True)
    Team_banner = models.ImageField(blank=True, null=True)

    Team_description = models.TextField(blank=True, null=True)

    Team_Form_Date_Time = models.DateTimeField(default=datetime.now(), blank=True)
