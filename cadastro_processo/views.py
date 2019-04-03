from django.shortcuts import render, redirect
from .forms import PlanilhaForm
from .models import Planilha
from processo.models import Processo

def home(request):
    context = {
        'planilhas': Planilha.objects.all()
    }
    return render(request, 'cadastro_processo/home.html', context=context)


def cadastro(request):
    if request.method == 'POST':
        form = PlanilhaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cadastro_processo:home')
    else:
        form = PlanilhaForm()
    return render(request, 'cadastro_processo/cadastro_processo.html', {'form': form})


def processo_detail(request, id):
    context = {
        'processos': Processo.objects.filter(cliente_id=id),
        'planilha': Planilha.objects.get(id=id)
    }
    return render(request, 'cadastro_processo/processo_detalhe.html', context=context)
