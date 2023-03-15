from django.db import models
from datetime import datetime
# Create your models here.






class Slide_Model(models.Model):
    class Meta:
        verbose_name_plural = 'Slide'

    Slide_title = models.CharField(max_length=256, blank=True, null=True)
    Slide_Image = models.ImageField(blank=True, null=True)


class Logo_Model(models.Model):
    class Meta:
        verbose_name_plural = 'Logo'

    Logo_Image = models.ImageField(blank=True, null=True)

