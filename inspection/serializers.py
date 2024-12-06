from rest_framework import serializers
from inspection.models import VehicleInspection


class VehicleInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInspection
        fields = '__all__'
