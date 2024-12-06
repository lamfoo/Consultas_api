from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('inspection.urls')),  # Inclui as URLs da API do app inspection
    path('api/v2/', include('plate.urls')),  # Inclui as URLs da API do app plate_registration
]
