from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('add', views.add_flight, name='add_flight'),
    path('remove/<int:flight_id>/', views.remove_flight, name='remove_flight'),
    path('flights', views.flight_list, name='flight_list'),
    # path('book/<int:flight_id>', views., name=''),
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('user_bookings/<str:user_id>/', views.user_bookings, name='user_bookings'),
]