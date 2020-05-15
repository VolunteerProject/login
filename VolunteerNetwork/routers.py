from Portal.api.viewsets import PortalViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('org',PortalViewSet , basename='org')
