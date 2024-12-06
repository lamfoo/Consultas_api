from dj_rql.filter_cls import AutoRQLFilterClass
from .models import PlateRegistration

class PlateRegistrationFilterClass(AutoRQLFilterClass):
    MODEL = PlateRegistration
    FILTERS = [
        {
            'filter': 'matricula',
            'source': 'matricula',
        },
        {
            'filter': 'marca',
            'source': 'marca',
        },
        {
            'filter': 'modelo',
            'source': 'modelo',
        },
        {
            'filter': 'ano_fabricacao',
            'source': 'ano_fabricacao',
        },
        {
            'filter': 'cor',
            'source': 'cor',
        },
        {
            'filter': 'categoria',
            'source': 'categoria',
        },
        {
            'filter': 'numero_registro',
            'source': 'numero_registro',
        },
        {
            'filter': 'local_registro',
            'source': 'local_registro',
        },
        {
            'filter': 'nome_proprietario',
            'source': 'nome_proprietario',
        },
        {
            'filter': 'data_emissao',
            'source': 'data_emissao',
        },
    ]
