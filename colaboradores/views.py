from django.shortcuts import render, redirect, get_object_or_404
from .models import Colaborador
from .forms import ColaboradorForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# Aqui encontram-se as operações CRUD de "Colaborador"

# Create
@login_required
def colaborador_create(request):
    # Cria um form novo ou pega um preenchido
    form = ColaboradorForm(request.POST or None, request.FILES or None)

    # Validando formulário e transformando-o em um objeto
    if form.is_valid():
        form.save()
        return redirect('colaborador_read')

    # Devolvendo o form para a minha página html
    return render(request, 'colaborador_form.html', {'form': form})

# Read
@login_required
def colaborador_read(request):
    nome = request.GET.get('nome', None)
    sobrenome = request.GET.get('sobrenome', None)

    if nome or sobrenome:
        colaborador = Colaborador.objects.filter(first_name__icontains=nome) | Colaborador.objects.filter(last_name__icontains=sobrenome)
    else:
        colaborador = Colaborador.objects.all()

    return render(request, 'colaboradores.html', {'colaborador': colaborador})

# Update
@login_required
def colaborador_update(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)
    form = ColaboradorForm(request.POST or None, request.FILES or None, instance=colaborador)

    if form.is_valid():
        form.save()
        return redirect('colaborador_read')

    return render(request, 'colaborador_form.html', {'form': form})

# Delete
@login_required
def colaborador_delete(request, id):
    colaborador = get_object_or_404(Colaborador, pk=id)

    if (request.method == 'POST'):
        colaborador.delete()
        return redirect('colaborador_read')

    return render(request, 'colaborador_confirmar_delete.html', {'colaborador': colaborador})