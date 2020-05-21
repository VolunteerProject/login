
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
  path('register/', views.RegisterView.as_view(), name='register'),
  path('login/', views.LoginView.as_view(), name='login'),
  path('', views.index, name='index'),  
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('confirm-email/<str:user_id>/<str:token>/', views.ConfirmRegistrationView.as_view(), name='confirm_email')
]   