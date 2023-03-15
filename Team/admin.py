from django.contrib import admin
from . models import Team_Model
# Register your models here.


@admin.register(Team_Model)
class Team_Model(admin.ModelAdmin):
    list_display = ['id', 'Manager', 'Team_Name', 'Team_Owner_Name', 'Team_Total_play_count']
