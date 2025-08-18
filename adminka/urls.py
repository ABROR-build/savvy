from django.urls import path
from . import views

urlpatterns = [
    # read-activities
    path('', views.ListTodayActivities.as_view(), name='list-todays-activities'),
    path('filter-services/', views.FilterServices.as_view(), name='filter-services'),
    path('filter-stationaries/', views.FilterStationaries.as_view(), name='filter-stationaries'),
    path('filter-expenses/', views.FilterExpenses.as_view(), name='filter-expenses'),
    path('filter/<str:username>/', views.FilterByUser.as_view(), name='filter-by-user'),
    path('filter-services-by/<str:username>/', views.FilterServicesByUser.as_view(), name='filter-services-by-user'),
    path('filter-stationaries-by/<str:username>/', views.FilterStationariesByUser.as_view(), name='filter-stationaries-by-user'),
    path('list-months/', views.ListMonths.as_view(), name='list-months'),
    path('list-days/', views.ListDays.as_view(), name='list-days'),

    # update-activities
    path('edit-activity-/<int:pk>/', views.EditActivity.as_view(), name='edit-activity'),
    path('edit-custom-activity-/<int:pk>/', views.EditCustomActivity.as_view(), name='edit-custom-activity'),
    path('edit-stationary-activity-/<int:pk>/', views.EditStationaryActivity.as_view(), name='edit-stationary-activity'),

    # delete-activities
    path('delete-activity-/<int:pk>/', views.DeleteActivity.as_view(), name='delete-activity'),
    path('delete-custom-activity-/<int:pk>/', views.DeleteCustomActivity.as_view(), name='delete-custom-activity'),
    path('delete-stationary-activity-/<int:pk>/', views.DeleteStationaryActivity.as_view(), name='delete-stationary-activity'),
]
