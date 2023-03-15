from django.urls import path
from . import views

urlpatterns = [
    path('find_individual_id/', views.find_individual_id, name='find_individual_id'),

]
