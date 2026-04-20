from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Cidade

class IndexView(TemplateView):
    template_name = "cadastros/index.html"

class CidadeCreate(CreateView):
    model = Cidade
    fields = ["nome", "estado"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cidade-list")
    extra_context = {
        "titulo": "Cadastrar Cidade",
        "botao": "Salvar"
    }

class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ["nome", "estado"]
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("cidade-list")
    extra_context = {
        "titulo": "Editar Cidade",
        "botao": "Atualizar"
    }

class CidadeDelete(DeleteView):
    model = Cidade
    template_name = "cadastros/form_delete.html"
    success_url = reverse_lazy("cidade-list")
    extra_context = {
        "titulo": "Excluir Cidade",
    }

class CidadeList(ListView):
    model = Cidade
    template_name = "cadastros/list.html"
    paginate_by = 10

class CidadeDetail(DetailView):
    model = Cidade
    template_name = "cadastros/detail.html"
