from django.contrib import admin
from . models import News_Model, News_catagory
# Register your models here.


@admin.register(News_Model)
class News_Model(admin.ModelAdmin):
    list_display = ['id', 'title','subtitle', 'category', 'News_Date_Time']

@admin.register(News_catagory)
class News_catagory(admin.ModelAdmin):
    list_display = ['id', 'Catagory']
