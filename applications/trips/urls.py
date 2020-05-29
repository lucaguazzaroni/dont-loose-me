from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.trip_listing),
    path('create/', views.trip_create),
    path('passengers/<int:trip_id>/', views.passengers_managment),
    path('stops/list/<int:trip_id>/', views.trip_stops_list),
    path('assistants/<int:assistant_id>/', views.assistants_managment),
    path('assistants/list/<int:stop_id>/', views.assistants_list),
]
