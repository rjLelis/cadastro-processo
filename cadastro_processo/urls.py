from django.urls import path
from . import views

app_name = 'cadastro_processo'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('processo/<int:id>', views.processo_detail, name='processo_detalhe')
]