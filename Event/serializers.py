# from rest_framework import serializers
# from datetime import datetime
#
#
# class Event_Model_serializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     Home_Team = serializers.CharField(max_length=256, allow_blank=True, allow_null=True)
#     Way_Team = serializers.CharField(max_length=256, allow_blank=True, allow_null=True)
#     Stadium_Name = serializers.CharField(max_length=256, allow_blank=True, allow_null=True)
#     Event_Date_Time = serializers.DateTimeField()
#

from rest_framework import serializers
from datetime import datetime

from .models import Event_Model
from rest_framework.serializers import ModelSerializer, ReadOnlyField
# from django.contrib.sites.models import Site
# from django.conf import settings


class Event_Model_serializer(serializers.ModelSerializer):
    class Meta:
        model=Event_Model
        fields="__all__"

