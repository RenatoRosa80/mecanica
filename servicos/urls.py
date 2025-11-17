from django.urls import path
from . import views

app_name = "servicos"

urlpatterns = [
    # serviços (cadastro de tipos de serviço)
    path("", views.ServicoListView.as_view(), name="index"),
    path("novo/", views.ServicoCreateView.as_view(), name="servico_create"),
    path("<int:pk>/editar/", views.ServicoUpdateView.as_view(), name="servico_update"),
    path("<int:pk>/excluir/", views.ServicoDeleteView.as_view(), name="servico_delete"),

    # ordens
    path("ordens/", views.OrdemListView.as_view(), name="ordens"),
    path("ordens/novo/", views.ordem_create, name="ordem_create"),
    path("ordens/<int:pk>/", views.OrdemDetailView.as_view(), name="ordem_detail"),
    path("ordens/<int:pk>/editar/", views.ordem_update, name="ordem_update"),
    path("ordens/<int:pk>/excluir/", views.OrdemDeleteView.as_view(), name="ordem_delete"),
    path("ordens/<int:pk>/concluir/", views.ordem_mark_concluded, name="ordem_concluir"),
]
