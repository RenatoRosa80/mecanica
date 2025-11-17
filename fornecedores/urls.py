from django.urls import path
from . import views

urlpatterns = [
    path('', views.fornecedor_list, name='fornecedor_list'),
    path('novo/', views.fornecedor_create, name='fornecedor_create'),
    path('editar/<int:pk>/', views.fornecedor_update, name='fornecedor_update'),
    path('excluir/<int:pk>/', views.fornecedor_delete, name='fornecedor_delete'),
]
