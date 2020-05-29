from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/', views.account_login),
    path('logout/', views.account_logout),
    #path('login/',auth_views.PasswordChangeView.as_view(template_name='accounts/login.html'), name='login'),
]