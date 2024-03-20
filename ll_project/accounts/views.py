from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    #cadastra um usuario novo
    if request.method != 'POST':
        #exibe o formulario em branco
        form = UserCreationForm()
    else: 
        #processa o formulario preenchido
        form = UserCreationForm(data = request.POST)
        #verifica se o formulario é valido
        if form.is_valid():
            new_user = form.save()
            #faz o login do usuario e o direciona para a pagina inicial
            login(request, new_user)
            return redirect('learning_logs:index')
    #exibi um formulario branco ou invalido 
    context = {'form': form}
    return render(request, 'registration/register.html', context)