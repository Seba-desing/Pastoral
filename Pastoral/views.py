from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import redirect, render
from .forms import CustomUserForm, UserCreationForm
from django.contrib.auth import login, authenticate

def index(request):
    return render(request,"index.html")
def tres(request):
    return render(request,"1_a_3.html")    
def seis(request):
    return render(request,"4_a_6.html")    
def registrar_usuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()

            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect(to='/index/')
    return render(request,'Registration/registrar.html',data)
def index2(request):
    return render(request,"index2.html")
def index3(request):
    return render(request,"index3.html")    
