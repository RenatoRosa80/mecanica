from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Servico, OrdemServico, OrdemItem
from .forms import ServicoForm, OrdemServicoForm, OrdemItemFormSet

# -----------------------
# Servico CRUD
# -----------------------
class ServicoListView(LoginRequiredMixin, ListView):
    model = Servico
    template_name = "servicos/list.html"
    context_object_name = "servicos"
    paginate_by = 20

class ServicoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "servicos.add_servico"
    model = Servico
    form_class = ServicoForm
    template_name = "servicos/form.html"
    success_url = reverse_lazy("servicos:index")

class ServicoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "servicos.change_servico"
    model = Servico
    form_class = ServicoForm
    template_name = "servicos/form.html"
    success_url = reverse_lazy("servicos:index")

class ServicoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "servicos.delete_servico"
    model = Servico
    template_name = "servicos/confirm_delete.html"
    success_url = reverse_lazy("servicos:index")

# -----------------------
# Ordem de Servico CRUD (com inline formset de itens)
# -----------------------
class OrdemListView(LoginRequiredMixin, ListView):
    model = OrdemServico
    template_name = "servicos/ordens_list.html"
    context_object_name = "ordens"
    paginate_by = 20

class OrdemDetailView(LoginRequiredMixin, DetailView):
    model = OrdemServico
    template_name = "servicos/ordem_detail.html"
    context_object_name = "ordem"

# Create + manage inline items
def ordem_create(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form = OrdemServicoForm(request.POST)
        formset = OrdemItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            ordem = form.save()
            items = formset.save(commit=False)
            for item in items:
                item.ordem = ordem
                # preenche preço unitário caso não venha (usa preço do serviço)
                if not item.preco_unitario:
                    item.preco_unitario = item.servico.preco
                item.save()
            return redirect(ordem.get_absolute_url())
    else:
        form = OrdemServicoForm()
        formset = OrdemItemFormSet()
    return render(request, "servicos/ordem_form.html", {"form": form, "formset": formset})

def ordem_update(request, pk):
    if not request.user.is_authenticated:
        return redirect("login")
    ordem = get_object_or_404(OrdemServico, pk=pk)
    if request.method == "POST":
        form = OrdemServicoForm(request.POST, instance=ordem)
        formset = OrdemItemFormSet(request.POST, instance=ordem)
        if form.is_valid() and formset.is_valid():
            ordem = form.save()
            items = formset.save(commit=False)
            # salvar e deletar apropriadamente
            for item in items:
                if not item.preco_unitario:
                    item.preco_unitario = item.servico.preco
                item.ordem = ordem
                item.save()
            for deleted in formset.deleted_objects:
                deleted.delete()
            return redirect(ordem.get_absolute_url())
    else:
        form = OrdemServicoForm(instance=ordem)
        formset = OrdemItemFormSet(instance=ordem)
    return render(request, "servicos/ordem_form.html", {"form": form, "formset": formset, "ordem": ordem})

class OrdemDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "servicos.delete_ordemservico"
    model = OrdemServico
    template_name = "servicos/confirm_delete_ordem.html"
    success_url = reverse_lazy("servicos:ordens")

# simple helper to mark concluded
def ordem_mark_concluded(request, pk):
    ordem = get_object_or_404(OrdemServico, pk=pk)
    ordem.status = "concluida"
    from django.utils import timezone
    ordem.data_conclusao = timezone.now()
    ordem.save()
    return redirect(ordem.get_absolute_url())
