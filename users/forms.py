from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import profile

class profileForm(ModelForm):
    class Meta:
        model = profile
        exclude = ['user']
        widgets = {
            'image' : forms.FileInput(),
            'displayname' : forms.TextInput(attrs={'placeholder':'Add a name U'}),
            'info' : forms.Textarea(attrs={'rows':3,'placeholder':'Add information quikk'})
        }


class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model  = User
        fields = ['email']