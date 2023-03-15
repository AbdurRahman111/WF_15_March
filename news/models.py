from django.db import models
from datetime import datetime
# Create your models here.



class News_catagory(models.Model):
    class Meta:
        verbose_name_plural = 'News_catagory'
    Catagory = models.CharField(max_length=256, blank=True, null=True)




class News_Model(models.Model):
    class Meta:
        verbose_name_plural = 'News'


    title = models.CharField(max_length=256, blank=True, null=True)
    subtitle = models.CharField(max_length=256, blank=True, null=True)
    photo = models.ImageField(upload_to="news_image/", blank=True, null=True)

    category = models.ForeignKey(News_catagory, on_delete=models.CASCADE, blank=True, null=True)
    Description = models.TextField(max_length=256, blank=True, null=True)
    video_link = models.TextField(max_length=256, blank=True, null=True)

    News_Date_Time = models.DateTimeField(default=datetime.now(), blank=True)

