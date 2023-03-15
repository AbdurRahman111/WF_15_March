from django.contrib import admin
from . models import Game_Model
# Register your models here.


@admin.register(Game_Model)
class Game_Model(admin.ModelAdmin):
    list_display = ['id', 'Event_for_game',  'Home_Team_Score', 'Way_Team_Score']
