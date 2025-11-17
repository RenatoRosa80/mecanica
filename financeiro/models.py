from django.db import models

class Lancamento(models.Model):
    TIPO_CHOICES = (
        ("E", "Entrada"),
        ("S", "Saída"),
    )

    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"
