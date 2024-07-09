from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListStationaries.as_view(), name='list-stationaries'),
    path('categories/', views.ListCategories.as_view(), name='list-categories'),
    path('filter/<int:pk>/', views.FilterStationaries.as_view(), name='filter-stationaries')
]
