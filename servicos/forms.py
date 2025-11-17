from django import forms
from django.forms import inlineformset_factory
from .models import Servico, OrdemServico, OrdemItem

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ["nome", "descricao", "preco", "ativo"]

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = ["cliente", "veiculo", "descricao", "status", "observacoes"]

# Inline formset para itens de ordem (será usado nas views)
OrdemItemFormSet = inlineformset_factory(
    OrdemServico,
    OrdemItem,
    fields=("servico", "preco_unitario", "quantidade"),
    extra=1,
    can_delete=True,
)
