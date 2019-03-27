from django.shortcuts import render
from .forms import PlanilhaForm

def cadastro(request):
    if request.method == 'POST':
        form = PlanilhaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            nome = form.cleaned_data.get('nome')
            print(f'Planilha do cliente {nome} cadastrada com sucesso')
    else:
        form = PlanilhaForm()
    return render(request, 'cadastro_processo/home.html', {'form': form})