#definindo padrões de URL para learning_logs 
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #pagina inicial
    #o name serve para que o index e etc virem um link lá no base.html e que nos consiga pular de uma pagina para outra só clicando nos links
    path('', views.index, name='index'),
    #paginas para mostrar todos os tópicos 
    path('topics/', views.topics, name= 'topics'),
    #pagina de detalhes para um unico topico
    path('topics/<int:topic_id>/', views.topic, name='topic' ), 
    #pagina para o usuario integarir e criar um novo topico
    path('new_topic/', views.new_topic, name='new_topic'),
    #Pagina para o usuario inserir as entradas dos topicos
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #é necessario que a url passe o id da pagina por isso
    path('edit_entry/<int:entry_id>/', views.edit_entry, name="edit_entry"), 
]