from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import FormTopic, EntryForm

# Create your views here.

def index(request): 
    #A pagina inicial para o registro de aprendizagem 
    return render(request, 'learning_logs/index.html')

def topics(request):
    #mostra todos os topicos 
    topics = Topic.objects.order_by('date_added')
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
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect ('learning_logs:topic', topic_id=topic_id)
    
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



