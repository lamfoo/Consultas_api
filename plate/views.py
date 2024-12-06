from dj_rql.drf import RQLFilterBackend
from rest_framework import viewsets
from .models import PlateRegistration
from .serializers import PlateRegistrationSerializer
from .filters import PlateRegistrationFilterClass

class PlateRegistrationViewSet(viewsets.ModelViewSet):
    queryset = PlateRegistration.objects.all()
    serializer_class = PlateRegistrationSerializer
    # Filtro RQL
    filter_backends = [RQLFilterBackend]
    rql_filter_class = PlateRegistrationFilterClass
