from django.contrib import admin
from . models import Slide_Model, Logo_Model
# Register your models here.


@admin.register(Slide_Model)
class Slide_Model(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Logo_Model)
class Logo_Model(admin.ModelAdmin):
    list_display = ['id']
