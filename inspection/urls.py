from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inspection.views import VehicleInspectionViewSet

# Cria o roteador e registra o ViewSet
router = DefaultRouter()
router.register('inspections', VehicleInspectionViewSet)

# Inclui as URLs geradas pelo roteador
urlpatterns = [
    path('', include(router.urls)),
]
