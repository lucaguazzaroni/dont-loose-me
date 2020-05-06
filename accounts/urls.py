from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.account_login),
    path('logout/', views.account_logout),
]