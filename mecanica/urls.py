from django.contrib import admin
from django.urls import path, include
from core import views  # <-- IMPORT NECESSÁRIO

urlpatterns = [
    path('', views.home, name='home'),

    path('clientes/', include('clientes.urls')),
    path('veiculos/', include('veiculos.urls')),
    path('servicos/', include('servicos.urls')),
    path('fornecedores/', include('fornecedores.urls')),
    path('estoque/', include('estoque.urls')),
    path('financeiro/', include('financeiro.urls')),
    path('relatorios/', include('relatorios.urls')),

    path('accounts/', include('django.contrib.auth.urls')),  # LOGIN
    path('admin/', admin.site.urls),
]
