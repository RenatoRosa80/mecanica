from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import Veiculo
from .forms import VeiculoForm

class VeiculoListView(LoginRequiredMixin, ListView):
    model = Veiculo
    template_name = "veiculos/list.html"
    context_object_name = "veiculos"
    paginate_by = 12

class VeiculoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = "veiculos/form.html"
    permission_required = "veiculos.add_veiculo"
    success_url = reverse_lazy("veiculos:index")

class VeiculoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = "veiculos/form.html"
    permission_required = "veiculos.change_veiculo"
    success_url = reverse_lazy("veiculos:index")

class VeiculoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Veiculo
    template_name = "veiculos/confirm_delete.html"
    permission_required = "veiculos.delete_veiculo"
    success_url = reverse_lazy("veiculos:index")

class VeiculoDetailView(LoginRequiredMixin, DetailView):
    model = Veiculo
    template_name = "veiculos/detail.html"
