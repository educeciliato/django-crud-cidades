from django.urls import path
from .views import IndexView, CidadeCreate, CidadeUpdate, CidadeDelete, CidadeList, CidadeDetail

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cidade-create'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='cidade-update'),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='cidade-delete'),
    path('listar/cidades/', CidadeList.as_view(), name='cidade-list'),
    path('detalhar/cidade/<int:pk>/', CidadeDetail.as_view(), name='cidade-detail'),
]
