from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.index, name="index"),
    path("funcionarios/", views.FuncionarioListView.as_view(), name="lista_funcionarios"),
]
