from django.contrib import admin
from .models import PlateRegistration

class PlateRegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'matricula', 'marca', 'modelo', 'ano_fabricacao', 
        'cor', 'categoria', 'numero_registro', 'local_registro', 
        'nome_proprietario', 'data_emissao'
    )
    search_fields = ('matricula', 'marca', 'modelo', 'numero_registro', 'nome_proprietario')
    list_filter = ('marca', 'ano_fabricacao', 'cor', 'categoria', 'data_emissao')

admin.site.register(PlateRegistration, PlateRegistrationAdmin)
