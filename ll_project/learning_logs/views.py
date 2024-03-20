from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import FormTopic, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

#request é a requisição do usuario
def index(request): 
    #A pagina inicial para o registro de aprendizagem 
    #render vai pegar o request e renderizar para uma pagina HTML com a caminho que definimos 
    return render(request, 'learning_logs/index.html')

def topics(request):
    #mostra todos os topicos 
    #order_by estou pegando o objeto no banco de dados e ordenados pela data
    topics = Topic.objects.order_by('date_added')
    #criei um dicionario de chave e valor
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    #Mostra um unico topico e todas as suas entradas 
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render (request, 'learning_logs/topic.html', context)

def new_topic(request):
    #adicionar um topico novo
    if request.method != 'POST': 
        #nenhum dado foi enviado; criar um formulario em branco
        form = FormTopic()
    else: 
        #dados do post enviados; processar os dados
        form = FormTopic(data=request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('learning_logs:topics')
    #exibi um formulario em branco ou inválido
    context = {'form':form}    
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    #adiciona uma nova entrada para o topico especifico
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST': 
        form = EntryForm()
    else: 
        #dados POST enviado, processando os dado 
        form = EntryForm(data=request.POST)
        if form.is_valid():
            #commit salva, faz basicamente um pré salvamento
            new_entry = form.save(commit=False)
            #agora sim peguei os dados do topico
            new_entry.topic = topic
            #agora sim posso salvar
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    #exibi um formulario branco ou invalido 
    context = {'topic':topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    #edita uma entrada existente
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        #REQUISIÇÃO INICIAL; pré-preenche formulario com a entrada atual 
        form = EntryForm(instance=entry)
    else: 
        #dados POST enviados; processar dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
        
    context = {'entry': entry, 'topic': topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)

#comentatiooos



