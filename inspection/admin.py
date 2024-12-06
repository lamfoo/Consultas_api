from django.contrib import admin
from .models import VehicleInspection

class VehicleInspectionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'matricula', 'modelo', 'marca', 'ano', 
        'km', 'n_ficha', 'data_criacao_inspecao', 'data_proxima_inspecao'
    )
    search_fields = ('matricula', 'modelo', 'marca', 'n_ficha')
    list_filter = ('marca', 'ano', 'data_criacao_inspecao', 'data_proxima_inspecao')

admin.site.register(VehicleInspection, VehicleInspectionAdmin)
