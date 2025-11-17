from django.urls import path
from . import views

urlpatterns = [
    path("", views.financeiro_list, name="financeiro_list"),
    path("novo/", views.financeiro_create, name="financeiro_create"),
    path("editar/<int:pk>/", views.financeiro_update, name="financeiro_update"),
    path("excluir/<int:pk>/", views.financeiro_delete, name="financeiro_delete"),
]
