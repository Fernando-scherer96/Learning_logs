#definindo padrões de URL para learning_logs 
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #pagina inicial
    path('', views.index, name='index'),
    #paginas para mostrar todos os tópicos 
    path('topics/', views.topics, name= 'topics'),
]