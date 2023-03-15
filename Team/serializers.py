from rest_framework import serializers
from datetime import datetime
from Player.serializers import Player_Model_serializer
from User_info.serializers import User_information_serializer
from Player.models import Player_Model
from .models import Team_Model
from rest_framework.serializers import ModelSerializer, ReadOnlyField
# from django.contrib.sites.models import Site
# from django.conf import settings


class Team_Model_serializer(serializers.ModelSerializer):

    # ae model ar kon field jay model ar foregnkey tar sathe serializer

    Team_player_1_id_from_Plyer_model = Player_Model_serializer()
    Team_player_2_id_from_Plyer_model = Player_Model_serializer()
    Team_player_3_id_from_Plyer_model = Player_Model_serializer()
    Team_player_4_id_from_Plyer_model = Player_Model_serializer()
    Team_player_5_id_from_Plyer_model = Player_Model_serializer()
    Team_player_6_id_from_Plyer_model = Player_Model_serializer()
    Team_player_7_id_from_Plyer_model = Player_Model_serializer()
    Team_player_8_id_from_Plyer_model = Player_Model_serializer()
    Team_player_9_id_from_Plyer_model = Player_Model_serializer()
    Team_player_10_id_from_Plyer_model = Player_Model_serializer()
    Team_player_11_id_from_Plyer_model = Player_Model_serializer()
    Team_player_12_id_from_Plyer_model = Player_Model_serializer()
    Team_player_13_id_from_Plyer_model = Player_Model_serializer()
    Team_player_14_id_from_Plyer_model = Player_Model_serializer()
    Team_player_15_id_from_Plyer_model = Player_Model_serializer()
    Team_player_16_id_from_Plyer_model = Player_Model_serializer()
    Team_player_17_id_from_Plyer_model = Player_Model_serializer()
    Team_player_18_id_from_Plyer_model = Player_Model_serializer()

    Team_player_active_1_id_from_Plyer_model = Player_Model_serializer()
    Team_player_active_2_id_from_Plyer_model = Player_Model_serializer()
    Team_player_active_3_id_from_Plyer_model = Player_Model_serializer()
    Team_player_active_4_id_from_Plyer_model = Player_Model_serializer()
    Team_player_active_5_id_from_Plyer_model = Player_Model_serializer()
    Team_player_active_6_id_from_Plyer_model = Player_Model_serializer()
    Team_player_active_7_id_from_Plyer_model = Player_Model_serializer()
    Team_player_active_8_id_from_Plyer_model = Player_Model_serializer()
    Team_player_active_9_id_from_Plyer_model = Player_Model_serializer()
    Team_player_active_10_id_from_Plyer_model = Player_Model_serializer()
    Team_player_active_11_id_from_Plyer_model = Player_Model_serializer()

    Team_player_substitute_1_id_from_Plyer_model = Player_Model_serializer()
    Team_player_substitute_2_id_from_Plyer_model = Player_Model_serializer()
    Team_player_substitute_3_id_from_Plyer_model = Player_Model_serializer()
    Team_player_substitute_4_id_from_Plyer_model = Player_Model_serializer()
    Team_player_substitute_5_id_from_Plyer_model = Player_Model_serializer()
    Team_player_substitute_6_id_from_Plyer_model = Player_Model_serializer()
    Team_player_substitute_7_id_from_Plyer_model = Player_Model_serializer()

    Team_captain = Player_Model_serializer()

    Manager = User_information_serializer()
    class Meta:
        model=Team_Model
        fields="__all__"


