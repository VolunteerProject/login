from . import views

from django.urls import path,include



urlpatterns=[
    path('',views.index,name="home"),

    path('login/',views.userlogin,name='login'),
    path('register/',views.registerView,name='register'),

]