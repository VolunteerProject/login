from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'token_save', views.VolunteerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),

    
    
    ] 
