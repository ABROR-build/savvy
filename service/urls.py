from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListServices.as_view(), name='list_services'),
    path('post/new/', views.PostCustomService.as_view(), name='post_new_service'),
    path('post/<int:pk>/', views.PostService.as_view(), name='post_service'),
    path('list_my_activities/', views.ListMyActivities.as_view(), name='list_my_activities')
]
