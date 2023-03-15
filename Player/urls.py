from django.urls import path
from . import views

urlpatterns = [
    path('find_all_player/', views.find_all_player, name='find_all_player'),
    path('find_one_player/', views.find_one_player, name='find_one_player'),
    path('create_player/', views.create_player, name='create_player'),
    path('player_delete/', views.player_delete, name='player_delete'),
    path('player_update/', views.player_update, name='player_update'),

]
