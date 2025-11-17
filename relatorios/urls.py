from django.urls import path
from . import views

urlpatterns = [
    path('', views.relatorios_home, name='relatorios_home'),

    path('financeiro/', views.relatorio_financeiro, name='relatorio_financeiro'),
    path('financeiro/pdf/', views.relatorio_financeiro_pdf, name='relatorio_financeiro_pdf'),
    path('financeiro/xlsx/', views.relatorio_financeiro_excel, name='relatorio_financeiro_excel'),

    path('clientes/', views.relatorio_clientes, name='relatorio_clientes'),
    path('clientes/pdf/', views.relatorio_clientes_pdf, name='relatorio_clientes_pdf'),

    path('estoque/', views.relatorio_estoque, name='relatorio_estoque'),
    path('estoque/pdf/', views.relatorio_estoque_pdf, name='relatorio_estoque_pdf'),
]
