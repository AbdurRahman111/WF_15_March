from django.urls import path
from . import views
urlpatterns = [
    path('find_individual_id/', views.find_individual_id, name='find_individual_id'),
    path('find_all/', views.find_all, name='find_all'),


]
