from django.contrib import admin
from .models import Servico, OrdemServico, OrdemItem

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "ativo", "criado_em")
    search_fields = ("nome",)
    list_filter = ("ativo",)

class OrdemItemInline(admin.TabularInline):
    model = OrdemItem
    extra = 1

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ("pk", "cliente", "veiculo", "status", "data_abertura")
    list_filter = ("status", "data_abertura")
    search_fields = ("cliente__nome", "veiculo__placa")
    inlines = (OrdemItemInline,)
