from django.db import models
from datetime import datetime
# Create your models here.


class FA_Model(models.Model):
    class Meta:
        verbose_name_plural = 'FA'

    category_CHOICES = (
        ('NEVER PLAYED', 'NEVER PLAYED'),
        ('PLAY SOMETIMES', 'PLAY SOMETIMES'),
        ('PLAY A LOT', 'PLAY A LOT'),
        ('WILDCATS', 'WILDCATS'),
    )
    subcategory_CHOICES = (
        ('GET INSPIRED', 'GET INSPIRED'),
        ('FOOTBALL STORIES', 'FOOTBALL STORIES'),
        ('FOOTBALL FITNESS', 'FOOTBALL FITNESS'),

    )

    title = models.CharField(max_length=256, blank=True, null=True)
    subtitle = models.CharField(max_length=256, blank=True, null=True)
    photo = models.ImageField(upload_to="news_image/", blank=True, null=True)

    category = models.CharField(max_length=256, choices=category_CHOICES, blank=True, null=True)
    subcategory = models.CharField(max_length=256, choices=subcategory_CHOICES, blank=True, null=True)
    Description = models.TextField(max_length=256, blank=True, null=True)
    video_link = models.TextField(max_length=256, blank=True, null=True)

    News_Date_Time = models.DateTimeField(default=datetime.now(), blank=True)

