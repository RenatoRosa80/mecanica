from django.shortcuts import render, redirect, get_object_or_404
from .models import Fornecedor
from .forms import FornecedorForm

def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores/fornecedor_list.html', {'fornecedores': fornecedores})

def fornecedor_create(request):
    form = FornecedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fornecedor_list')
    return render(request, 'fornecedores/fornecedor_form.html', {'form': form, 'titulo': 'Novo Fornecedor'})

def fornecedor_update(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    form = FornecedorForm(request.POST or None, instance=fornecedor)
    if form.is_valid():
        form.save()
        return redirect('fornecedor_list')
    return render(request, 'fornecedores/fornecedor_form.html', {'form': form, 'titulo': 'Editar Fornecedor'})

def fornecedor_delete(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('fornecedor_list')
    return render(request, 'fornecedores/fornecedor_confirm_delete.html', {'fornecedor': fornecedor})
