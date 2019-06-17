from rest_framework import fields, serializers
from .models import *

class SeatSerializer(serializers.ModelSerializer):

    auditorium = serializers.CharField(source='auditorium.name', read_only=True)
    class Meta:
        model = Seat
        fields = '__all__'
