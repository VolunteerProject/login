from Portal.api.serializers import OrgSerializer
from Portal.models import Organization
from rest_framework import viewsets


class PortalViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrgSerializer



