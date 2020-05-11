from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.trip_listing),
    path('create/', views.trip_create),
    path('passengers/<int:trip_id>/', views.passengers_managment),
    path('stops/<int:trip_id>/', views.trip_stops_list),
]
