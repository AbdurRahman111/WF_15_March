from django.contrib import admin
from . models import User_information
# Register your models here.


@admin.register(User_information)
class User_information(admin.ModelAdmin):
    list_display = ['id', 'User_Roll', 'User_Name']
