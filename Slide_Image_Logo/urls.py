from django.urls import path
from . import views

urlpatterns = [
    path('find_all_Slide_logo/', views.find_all_Slide_logo, name='find_all_Slide_logo'),
    path('create_Slider/', views.create_Slider, name='create_Slider'),
    path('delete_Slide_logo_with_id/', views.delete_Slide_logo_with_id, name='delete_Slide_logo_with_id'),

    path('find_last_main_logo/', views.find_last_main_logo, name='find_last_main_logo'),
    path('create_main_logo/', views.create_main_logo, name='create_main_logo'),

]
