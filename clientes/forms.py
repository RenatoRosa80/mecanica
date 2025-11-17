from django import forms
from .models import Cliente
import re
from django.core.exceptions import ValidationError

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "cpf", "telefone", "email", "endereco", "observacoes"]
        widgets = {
            "endereco": forms.Textarea(attrs={"rows": 2}),
            "observacoes": forms.Textarea(attrs={"rows": 3}),
        }

    CPF_RE = re.compile(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$")

    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")
        if cpf:
            if not self.CPF_RE.match(cpf):
                raise ValidationError("CPF deve ter o formato 000.000.000-00")
        return cpf
