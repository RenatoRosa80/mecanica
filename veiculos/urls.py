from django.urls import path
from . import views

app_name = "veiculos"

urlpatterns = [
    path("", views.VeiculoListView.as_view(), name="index"),
    path("novo/", views.VeiculoCreateView.as_view(), name="create"),
    path("<int:pk>/", views.VeiculoDetailView.as_view(), name="detail"),
    path("<int:pk>/editar/", views.VeiculoUpdateView.as_view(), name="update"),
    path("<int:pk>/excluir/", views.VeiculoDeleteView.as_view(), name="delete"),
]
