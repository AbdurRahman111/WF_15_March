from django.contrib import admin
from . models import Goal_Model
# Register your models here.


@admin.register(Goal_Model)
class Goal_Model(admin.ModelAdmin):
    list_display = ['id', 'Event_for_goal','Home_Team_Goal_Count_In_1', 'Way_Team_Goal_Count_In_1', 'Scorer_Name', 'Goal_Assist_Name', 'Goal_Date_Time']
