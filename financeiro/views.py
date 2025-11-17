from django.shortcuts import render, redirect, get_object_or_404
from .models import Lancamento
from .forms import LancamentoForm

def financeiro_list(request):
    lancamentos = Lancamento.objects.all().order_by("-data")
    return render(request, "financeiro/financeiro_list.html", {"lancamentos": lancamentos})


def financeiro_create(request):
    form = LancamentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("financeiro_list")
    
    return render(request, "financeiro/financeiro_form.html", {"form": form, "titulo": "Novo Lançamento"})


def financeiro_update(request, pk):
    lancamento = get_object_or_404(Lancamento, pk=pk)
    form = LancamentoForm(request.POST or None, instance=lancamento)

    if form.is_valid():
        form.save()
        return redirect("financeiro_list")

    return render(request, "financeiro/financeiro_form.html", {"form": form, "titulo": "Editar Lançamento"})


def financeiro_delete(request, pk):
    lancamento = get_object_or_404(Lancamento, pk=pk)

    if request.method == "POST":
        lancamento.delete()
        return redirect("financeiro_list")

    return render(request, "financeiro/financeiro_delete.html", {"lancamento": lancamento})
