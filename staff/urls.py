from django.urls import path
from . import views


urlpatterns = [
    path('Registration/', views.Register.as_view(), name='registration'),
    path('', views.Login.as_view(), name='Login'),
    path('Logout/', views.Logout.as_view(), name='Logout')

]
