from django.contrib import admin
from . models import Player_Model
# Register your models here.


@admin.register(Player_Model)
class Player_Model(admin.ModelAdmin):
    list_display = ['PLayer_Name', 'id', 'PLayer_Jersey', 'PLayer_Position', 'PLayer_Age', 'Base_price', 'Sell_price']
