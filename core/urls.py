from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('', core_views.home, name='home'),

    path('clientes/', include('clientes.urls')),
    path('veiculos/', include('veiculos.urls')),
    path('servicos/', include('servicos.urls')),
    path('fornecedores/', include('fornecedores.urls')),
    path('estoque/', include('estoque.urls')),
    path('financeiro/', include('financeiro.urls')),
    path('relatorios/', include('relatorios.urls')),

    path('admin/', admin.site.urls),
]
