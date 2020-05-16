from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth.views import logout
from . import views


urlpatterns=[
    path('login/',views.userlogin,name='login'),


    #path('', include('social_django.urls', namespace='social')),  # for signing up with google accounts
    #path('',include("django.contrib.auth.urls")),  # for authentication with google accounts
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL} , name='logout'),
    path('register/',views.registerView,name='register'),


]