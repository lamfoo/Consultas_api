from dj_rql.drf import RQLFilterBackend
from rest_framework import viewsets
from inspection.models import VehicleInspection
from inspection.serializers import VehicleInspectionSerializer
from inspection.filters import VehicleInspectionFilterClass

class VehicleInspectionViewSet(viewsets.ModelViewSet):
    queryset = VehicleInspection.objects.all()
    serializer_class = VehicleInspectionSerializer
    #filtro RQL
    filter_backends = [RQLFilterBackend]
    rql_filter_class = VehicleInspectionFilterClass
