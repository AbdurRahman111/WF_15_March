from rest_framework import serializers
from datetime import datetime

from .models import FA_Model
from rest_framework.serializers import ModelSerializer, ReadOnlyField
# from django.contrib.sites.models import Site
# from django.conf import settings


class FA_Model_serializer(serializers.ModelSerializer):
    class Meta:
        model=FA_Model
        fields="__all__"




