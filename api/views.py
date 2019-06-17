from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view,permission_classes,action
from rest_framework import permissions, viewsets
from .serializers import *

class SeatViewSet(viewsets.ModelViewSet):
    """
    Handles Notification request that comes from frontend.
    """
    queryset            = Seat.objects.all()
    serializer_class    = SeatSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        queryset = self.queryset
        auditorium_name = self.request.query_params.get('auditorium_name', None)
        if auditorium_name:
            queryset = queryset.filter(auditorium__name__iexact=auditorium_name)
        return queryset
