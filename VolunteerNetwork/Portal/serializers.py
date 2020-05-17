from rest_framework import serializers

from .models import Volunteer


class VolunteerSerializer(serializers.ModelSerializer):
    code = serializers.CharField(source='oauth_code')
    class Meta:
        model=Volunteer
        fields=['code', 'state']
