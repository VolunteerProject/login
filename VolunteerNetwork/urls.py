
from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path

from Portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Portal/',include('Portal.urls')),
    url(r'^$', views.index, name='index'),
]
