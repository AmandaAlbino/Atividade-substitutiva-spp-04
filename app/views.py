from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

# pagina inicial
def home(request):
    return render(request,'home.html')

#Formulario para cadastro
def create(request):
    return render(request,'create.html')

#coleta de dados dos usuarios
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
       data['msg']= 'Senha e confirmação de senha diferentes!'
       data['class']= 'alert-danger'
    else:
       user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
       user.first_name = request.POST['name']
       user.save()
       data['msg']= 'Usuario cadastrado com sucesso!'
       data['class']= 'alert-sucess'

    return render(request,'create.html',data)

#Formulário do painel de login
def painel(request):
    return render(request,'painel.html')

#Processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'painel.html',data)

#Página inicial do dashboard
def dashboard(request):
    return render(request,'dashboard/home.html')


