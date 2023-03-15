from django.contrib import admin
from . models import FA_Model
# Register your models here.


@admin.register(FA_Model)
class FA_Model(admin.ModelAdmin):
    list_display = ['id', 'title','subtitle', 'category', 'subcategory', 'News_Date_Time']
