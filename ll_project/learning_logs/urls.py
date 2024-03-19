#definindo padrões de URL para learning_logs 
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #pagina inicial
    path('', views.index, name='index'),
    #paginas para mostrar todos os tópicos 
    path('topics/', views.topics, name= 'topics'),
    #pagina de detalhes para um unico topico
    path('topics/<int:topic_id>/', views.topic, name='topic' ), 
    #pagina para o usuario integarir e criar um novo topico
    path('new_topic/', views.new_topic, name='new_topic'),
]