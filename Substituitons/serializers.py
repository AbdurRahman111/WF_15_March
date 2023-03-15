from rest_framework import serializers
from datetime import datetime
from Event.models import Event_Model
from Event.serializers import Event_Model_serializer
from .models import Substituitons_Model
from rest_framework.serializers import ModelSerializer, ReadOnlyField


class Substituitons_Model_serializer(serializers.ModelSerializer):


    event_Substituitons_here = Event_Model_serializer(read_only=True, many=True)
    class Meta:
        model=Substituitons_Model
        fields="__all__"


