from rest_framework import serializers
from datetime import datetime

from .models import News_Model, News_catagory
from rest_framework.serializers import ModelSerializer, ReadOnlyField
# from django.contrib.sites.models import Site
# from django.conf import settings


class News_Model_serializer(serializers.ModelSerializer):
    # img_url = serializers.SerializerMethodField()
    class Meta:
        model=News_Model
        fields="__all__"

class News_catagory_Model_serializer(serializers.ModelSerializer):
    # img_url = serializers.SerializerMethodField()
    class Meta:
        model=News_catagory
        fields="__all__"

    # def get_img_url(self, obj):
    #     if settings.DEBUG:  # debug enabled for dev and stage
    #         return 'http://%s%s%s' % (Site.objects.get_current().domain, settings.MEDIA_URL, obj.img.url)
    #     return obj.img.url


