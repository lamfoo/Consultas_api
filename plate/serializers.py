from rest_framework import serializers
from .models import PlateRegistration


class PlateRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlateRegistration
        fields = '__all__'
