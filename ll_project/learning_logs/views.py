from django.shortcuts import render, redirect
from .models import Topic
from .forms import FormTopic

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