from django.urls import path
from . import views

urlpatterns = [
    path('create_specific_taem/', views.create_specific_taem, name='create_specific_taem'),
    path('find_all_team/', views.find_all_team, name='find_all_team'),
    path('find_team_with_id/', views.find_team_with_id, name='find_team_with_id'),
    path('find_team_with_team_name/', views.find_team_with_team_name, name='find_team_with_team_name'),
    path('find_all_manager/', views.find_all_manager, name='find_all_manager'),
    path('delete_team/', views.delete_team, name='delete_team'),
    path('update_specific_taem/', views.update_specific_taem, name='update_specific_taem'),

]
