from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import  messages
# Create your views here.

#def index(request):
#    return redirect('/agenda/')#um dos metodos para redirect



@login_required(login_url='/login/') # == se não estiver logado não acessa a agenda
def lista_eventos(request):
    usuario = request.user
    #usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)#filter usuario, aparece só os eventos da pessoa logada//se eu tirar filter e colocar all() mostra todos os eventos
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect(('/'))
        else:
            messages.error(request, 'Usuário ou senha inválido')
    return redirect('/')


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        dataEvento = request.POST.get('dataEvento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              dataEvento=dataEvento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')

