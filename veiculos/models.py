from django.db import models
from django.urls import reverse
from clientes.models import Cliente

class Veiculo(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="veiculos",
        verbose_name="Cliente",
    )
    marca = models.CharField("Marca", max_length=100)
    modelo = models.CharField("Modelo", max_length=100)
    ano = models.PositiveIntegerField("Ano")
    placa = models.CharField("Placa", max_length=10, unique=True)
    cor = models.CharField("Cor", max_length=50, blank=True)
    observacoes = models.TextField("Observações", blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        ordering = ("-criado_em",)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"

    def get_absolute_url(self):
        return reverse("veiculos:detail", args=[self.pk])
