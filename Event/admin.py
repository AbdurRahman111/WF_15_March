from django.contrib import admin
from . models import Event_Model
# Register your models here.


@admin.register(Event_Model)
class Event_Model(admin.ModelAdmin):
    list_display = ['id', 'Home_Team', 'Way_Team', 'Stadium_Name', 'Event_Date_Time']
