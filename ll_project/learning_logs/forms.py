from django import forms

from .models import Topic, Entry

class FormTopic(forms.ModelForm):
    class Meta: 
        model = Topic
        fields = ['text']
        #tiramos o nosso labels
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta: 
        model = Entry
        fields = ['text']
        labels = {'Text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}