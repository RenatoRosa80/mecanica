from django.contrib import admin
from .models import Veiculo

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ("marca", "modelo", "ano", "placa", "cliente", "criado_em")
    search_fields = ("marca", "modelo", "placa", "cliente__nome")
    list_filter = ("marca", "ano", "criado_em")
    ordering = ("-criado_em",)
