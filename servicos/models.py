from django.db import models
from django.urls import reverse
from clientes.models import Cliente
from veiculos.models import Veiculo
from decimal import Decimal

class Servico(models.Model):
    nome = models.CharField("Serviço", max_length=200)
    descricao = models.TextField("Descrição", blank=True)
    preco = models.DecimalField("Preço", max_digits=10, decimal_places=2, default=0)
    ativo = models.BooleanField("Ativo", default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        ordering = ("-criado_em",)

    def __str__(self):
        return f"{self.nome} — R$ {self.preco}"

    def get_absolute_url(self):
        return reverse("servicos:index")


class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ("aberta", "Aberta"),
        ("em_andamento", "Em andamento"),
        ("aguardando_pecas", "Aguardando peças"),
        ("concluida", "Concluída"),
        ("cancelada", "Cancelada"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="ordens")
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT, related_name="ordens")
    descricao = models.TextField("Descrição do problema/serviço", blank=True)
    status = models.CharField("Status", max_length=30, choices=STATUS_CHOICES, default="aberta")
    data_abertura = models.DateTimeField("Aberta em", auto_now_add=True)
    data_conclusao = models.DateTimeField("Concluída em", null=True, blank=True)
    observacoes = models.TextField("Observações", blank=True)

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"
        ordering = ("-data_abertura",)

    def __str__(self):
        return f"OS #{self.pk} — {self.cliente} — {self.veiculo}"

    def total(self):
        total = Decimal("0.00")
        for item in self.itens.all():
            total += item.subtotal()
        return total

    def get_absolute_url(self):
        return reverse("servicos:ordem_detail", args=[self.pk])


class OrdemItem(models.Model):
    ordem = models.ForeignKey(OrdemServico, on_delete=models.CASCADE, related_name="itens")
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField("Quantidade", default=1)
    preco_unitario = models.DecimalField("Preço unitário", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Item da Ordem"
        verbose_name_plural = "Itens da Ordem"

    def __str__(self):
        return f"{self.servico.nome} x{self.quantidade}"

    def subtotal(self):
        return (self.preco_unitario or 0) * (self.quantidade or 0)
