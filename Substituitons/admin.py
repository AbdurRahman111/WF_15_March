from django.contrib import admin
from . models import Substituitons_Model
# Register your models here.


@admin.register(Substituitons_Model)
class Substituitons_Model(admin.ModelAdmin):
    list_display = ['id', 'Event_for_goal', 'PLayer_Name', 'Substituitons_Name']
