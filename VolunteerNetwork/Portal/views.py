from django.shortcuts import render
from rest_framework import viewsets,mixins,status
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from .serializers import VolunteerSerializer
from .models import Volunteer


class VolunteerViewSet(mixins.CreateModelMixin,
                       GenericViewSet):
    queryset = Volunteer.objects.all().order_by('user_id')
    serializer_class = VolunteerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)






