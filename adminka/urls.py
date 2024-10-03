from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTodayActivities.as_view(), name='list-todays-activities'),
    path('filter-services/', views.FilterServices.as_view(), name='filter-services'),
    path('filter-stationaries/', views.FilterStationaries.as_view(), name='filter-stationaries'),
    path('filter/<str:username>/', views.FilterByUser.as_view(), name='filter-by-user'),
    path('filter-services-by/<str:username>/', views.FilterServicesByUser.as_view(), name='filter-services-by-user'),
    path('filter-stationaries-by/<str:username>/', views.FilterStationariesByUser.as_view(), name='filter-stationaries-by-user'),
]