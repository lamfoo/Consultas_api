from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlateRegistrationViewSet

# Cria o roteador e registra o ViewSet
router = DefaultRouter()
router.register('plate-registrations', PlateRegistrationViewSet)

# Inclui as URLs geradas pelo roteador
urlpatterns = [
    path('', include(router.urls)),
]
