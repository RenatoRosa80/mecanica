from django import forms
from .models import Lancamento

class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
        fields = ["descricao", "valor", "data", "tipo"]

        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}),
        }
