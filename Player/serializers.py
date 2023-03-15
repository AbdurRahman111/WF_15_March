from rest_framework import serializers
from datetime import datetime

from .models import Player_Model
from rest_framework.serializers import ModelSerializer, ReadOnlyField
# from django.contrib.sites.models import Site
# from django.conf import settings


class Player_Model_serializer(serializers.ModelSerializer):
    class Meta:
        model=Player_Model
        fields="__all__"



