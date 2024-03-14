from django.db import models

# Create your models here.
class Topic(models.Model):
    '''Um tópico que o usuario está apreendendo'''
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

class Entry(models.Model): 
    #algo especifico apreendido sobre o modulo
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta: 
        verbose_name_plural = 'entries'

    def __str__(self): 
        #retorna a representação da string do modelo
        return f"{self.text[:50]}..."
    