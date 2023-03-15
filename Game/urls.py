from django.urls import path
from . import views

urlpatterns = [
    path('find_all_Game/', views.find_all_Game, name='find_all_Game'),
    path('find_game_with_id/', views.find_game_with_id, name='find_game_with_id'),
    path('find_game_with_Event_id/', views.find_game_with_Event_id, name='find_game_with_Event_id'),
    # path('game_for_live_show_with_all_info/', views.game_for_live_show_with_all_info, name='game_for_live_show_with_all_info'),
    path('create_specific_game/', views.create_specific_game, name='create_specific_game'),

]