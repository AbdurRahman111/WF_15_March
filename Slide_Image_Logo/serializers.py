from rest_framework import serializers
from datetime import datetime

from .models import Slide_Model, Logo_Model
from rest_framework.serializers import ModelSerializer, ReadOnlyField
# from django.contrib.sites.models import Site
# from django.conf import settings


class Slide_Model_Model_serializer(serializers.ModelSerializer):
    class Meta:
        model=Slide_Model
        fields="__all__"

class Logo_Model_Model_serializer(serializers.ModelSerializer):
    class Meta:
        model=Logo_Model
        fields="__all__"


