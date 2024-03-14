from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request): 
    #A pagina inicial para o registro de aprendizagem 
    return render(request, 'learning_logs/index.html')

def topics(request):
    #mostra todos os topicos 
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)