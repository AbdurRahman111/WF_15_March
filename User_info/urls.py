from django.urls import path
from . import views

urlpatterns = [
    path('find_user/', views.find_user, name='find_user'),
    path('create_user/', views.create_user, name='create_user'),

]
