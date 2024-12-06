import uuid
from django.db import models

class PlateRegistration(models.Model):
    matricula = models.CharField(max_length=20, unique=True, verbose_name="Matrícula")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    modelo = models.CharField(max_length=50, verbose_name="Modelo")
    ano_fabricacao = models.PositiveIntegerField(verbose_name="Ano de Fabricação")
    cor = models.CharField(max_length=30, verbose_name="Cor")
    tipo_veiculo = models.CharField(max_length=50, verbose_name="Tipo de Veículo")
    categoria = models.CharField(max_length=50, verbose_name="Categoria")
    numero_motor = models.CharField(max_length=50, verbose_name="Número do Motor")
    numero_quadro = models.CharField(max_length=50, verbose_name="Número do Quadro")
    nome_proprietario = models.CharField(max_length=100, verbose_name="Nome Completo do Proprietário")
    endereco_rua = models.CharField(max_length=100, verbose_name="Rua")
    endereco_numero = models.CharField(max_length=10, verbose_name="Número")
    endereco_bairro = models.CharField(max_length=50, verbose_name="Bairro")
    endereco_cidade = models.CharField(max_length=50, verbose_name="Cidade")
    endereco_provincia = models.CharField(max_length=50, verbose_name="Província")
    endereco_codigo_postal = models.CharField(max_length=20, verbose_name="Código Postal")
    data_emissao = models.DateField(verbose_name="Data de Emissão")
    numero_registro = models.CharField(max_length=10, unique=True, blank=True, editable=False,verbose_name="Número do Registro")
    local_registro = models.CharField(max_length=100, verbose_name="Local de Registro")
    documento_identidade = models.CharField(max_length=50, verbose_name="Documento de Identidade")

    class Meta:
        verbose_name = "Registro de Matrícula"
        verbose_name_plural = "Registros de Matrículas"

    def save(self, *args, **kwargs):
        # Gera um número único para numero_registro, se ainda não definido
        if not self.numero_registro:
            while True:
                generated_number = str(uuid.uuid4().int)[-6:]  # Gera 6 dígitos únicos
                if not PlateRegistration.objects.filter(numero_registro=generated_number).exists():
                    self.numero_registro = generated_number
                    break
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.matricula} - {self.nome_proprietario}"
