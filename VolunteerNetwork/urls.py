
from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from .routers import router

from Portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Portal/',include('Portal.urls')),
    path('', views.home, name='home'),
    path('api/',include(router.urls)),
    path('accounts/', include('allauth.urls')),


]
