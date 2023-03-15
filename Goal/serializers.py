from rest_framework import serializers
from datetime import datetime
from Event.models import Event_Model
from Event.serializers import Event_Model_serializer
from .models import Goal_Model
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class Goal_Model_serializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    #
    # # Event_for_goal = serializers.ForeignKey(Event_Model, on_delete=models.CASCADE, allow_blank=True, allow_null=True)
    # # Event_for_goal = serializers.RelatedField(source='Event_Model', read_only=True)
    # event_name = serializers.ReadOnlyField()
    #
    # Home_Team_Goal_Count_In_1 = serializers.CharField(max_length=256, allow_blank=True, allow_null=True)
    # Way_Team_Goal_Count_In_1 = serializers.CharField(max_length=256, allow_blank=True, allow_null=True)
    # Scorer_Name = serializers.CharField(max_length=256, allow_blank=True, allow_null=True)
    # Goal_Assist_Name = serializers.CharField(max_length=256, allow_blank=True, allow_null=True)
    #
    # Goal_Date_Time = serializers.DateTimeField(default=datetime.now())

    event_here = Event_Model_serializer(read_only=True, many=True)
    class Meta:
        model=Goal_Model
        fields="__all__"


