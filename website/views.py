from django.shortcuts import render, redirect
from website.models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        data = Coach()
        data.nome = request.POST['nome']
        data.frase = request.POST['frase'] 
        data.inspirador = request.POST['inspirador']
        data.save()

        args = {
            'sucesso': 'Você conseguiu campeão! Grite: Alucinação!'
        }

        return render(request, 'index.html', args)

    return render(request, 'index.html') 

def listar_coachs(request):
    listar_coachs = Coach.objects.filter(ativo=True).all()
    args = {
        'listar_coachs': listar_coachs
    }
    return render(request, 'listar_coachs.html', args)

def delete_coach(request, id):
    item = Coach.objects.get(id=id)
    if item is not None:
        item.ativo = False
        item.save()
        return redirect('/coachs/listar')
    return render (request, 'listar_coachs.html', {'msg': 'apagou'})
