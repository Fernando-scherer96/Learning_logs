from django import forms

from .models import Topic

class FormTopic(forms.ModelForm):
    class Meta: 
        model = Topic
        fields = ['text']
        labels = {'text': ''}