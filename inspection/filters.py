from dj_rql.filter_cls import AutoRQLFilterClass
from inspection.models import VehicleInspection

class VehicleInspectionFilterClass(AutoRQLFilterClass):
    MODEL = VehicleInspection
    FILTERS = [
        {
            'filter': 'marca',
            'source': 'marca',
        },
        {
            'filter': 'modelo',
            'source': 'modelo',
        },
        {
            'filter': 'matricula',
            'source': 'matricula',
        },
        {
            'filter': 'ano',
            'source': 'ano',
        },
        {
            'filter': 'km',
            'source': 'km',
        },
        {
            'filter': 'data_criacao',
            'source': 'data_criacao_inspecao',
        },
        {
            'filter': 'data_proxima',
            'source': 'data_proxima_inspecao',
        },
    ]
