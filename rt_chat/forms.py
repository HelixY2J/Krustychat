from django.forms import ModelForm
from django import forms
from .models import *

class Chatmsgform(ModelForm):
    class Meta:
        model = grpMsg
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder':'Send it dude...','class':'p-4 text-black', 'maxlength' : '300', 'autofocus': True}),

        }