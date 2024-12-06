import uuid
from django.db import models

class VehicleInspection(models.Model):
    matricula = models.CharField(max_length=50, verbose_name='Matrícula')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    marca = models.CharField(max_length=100, verbose_name='Marca')
    n_quadro = models.CharField(max_length=100, verbose_name='Número do Quadro')
    n_motor = models.CharField(max_length=100, verbose_name='Número do Motor')
    ano = models.PositiveIntegerField(verbose_name='Ano')
    km = models.PositiveIntegerField(verbose_name='Quilometragem')
    data_criacao_inspecao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação da Inspeção')
    data_proxima_inspecao = models.DateField(verbose_name='Data da Próxima Inspeção')
    deficiencias = models.TextField(null=True, blank=True, verbose_name='Deficiências')
    n_ficha = models.CharField(max_length=6, unique=True, editable=False, verbose_name='Número da Ficha')

    class Meta:
        ordering = ['matricula']
        verbose_name = 'Inspeção Veicular'
        verbose_name_plural = 'Inspeções Veiculares'

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.matricula}"

    def save(self, *args, **kwargs):
        if not self.n_ficha:
            while True:
                generated_number = str(uuid.uuid4().int)[-6:]
                if not VehicleInspection.objects.filter(n_ficha=generated_number).exists():
                    self.n_ficha = generated_number
                    break
        super().save(*args, **kwargs)
