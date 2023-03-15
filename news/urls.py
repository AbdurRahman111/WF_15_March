from django.urls import path
from . import views

urlpatterns = [
    path('find_all_news/', views.find_all_news, name='find_all_news'),
    path('find_news_with_category/', views.find_news_with_category, name='find_news_with_category'),
    path('create_specific_news/', views.create_specific_news, name='create_specific_news'),
    path('news_category/', views.news_category, name='news_category'),
    path('news_category_create/', views.news_category_create, name='news_category_create'),
    path('news_category_delete/', views.news_category_delete, name='news_category_delete'),
    path('news_delete/', views.news_delete, name='news_delete'),
    path('news_update/', views.news_update, name='news_update'),

]
