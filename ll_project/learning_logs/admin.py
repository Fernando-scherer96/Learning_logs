from django.contrib import admin

from .models import Topic, Entry

# Register your models here.
#informa ao django para gerenciar o nosso modelo por meio do site admin
admin.site.register(Topic)
admin.site.register(Entry)
