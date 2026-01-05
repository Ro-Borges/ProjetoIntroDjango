from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from helloworld.models import Funcionario

def index(request):
    return render(request, "website/index.html")

class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"