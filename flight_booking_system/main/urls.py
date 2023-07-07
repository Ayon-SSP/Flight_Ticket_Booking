from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('add', views.add_flight, name='add_flight'),
    path('remove/<int:flight_id>/', views.remove_flight, name='remove_flight'),
]