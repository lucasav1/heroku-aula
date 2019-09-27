from django.shortcuts import render, redirect
from website.models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        data_usuario = Usuario()
        data_usuario.email = request.POST['email']
        #aqui cria o algoritmo de criptografia
        data_usuario.senha = request.POST['senha']
        data_usuario.save()

        data_coach = Coach()
        data_coach.nome = request.POST['nome']
        data_coach.frase = request.POST['frase']
        data_coach.usuario = data_usuario
        data_coach.inspirador = request.POST['inspirador']
        data_coach.save()

        args = {
            'sucesso': 'Você conseguiu campeão! Grite: Alucinação!'
        }

        return render(request, 'login.html', args)

    return render(request, 'index.html')

def listar_coachs(request):
    listar_coachs = Coach.objects.filter(ativo=True).all()

    args = None
    if listar_coachs.first() is None:
            args = {
                'msg': 'Ops, Não tem ninguém aqui!'
            }
    else:
        args = {
            'listar_coachs': listar_coachs
        }

    return render(request, 'listar_coachs.html', args)

def delete_coach(request, id):
    item = Coach.objects.filter(id=id).first()
    if item is not None:
        item.ativo = False
        item.save()
        return redirect('/coachs/listar')
    return redirect('/')

def login(request):
    if request.method == "POST":
        formulario_email = request.POST['email']
        formulario_senha = request.POST['senha']

        usuario_logado = Coach.objects.filter(usuario__email = formulario_email,
                                              usuario__senha = formulario_senha).first()

        if usuario_logado is not None:
            args = {
                'dados': usuario_logado
            }
            return render(request, 'xablau.html', args)
        else:
            args = {
                'msg': 'Noooooosssa, credenciais inválidas'
            }
            return render(request, 'login.html', args)

    return render(request, 'login.html')
