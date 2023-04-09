from django import forms
from django.forms import ModelForm
from Coder.models import Players, Questions, Answers

class FormPlayers(ModelForm):
    class Meta:
        model = Players
        fields = [
            'first_name', 
            'last_name', 
            'date_birth' ,
            'phone',
            'adress', 
            'city',
            'state', 
            'country', 
            'dni',
        ]

    # def __init__(self, *args, **kwargs):
    #     super(FormPlayers, self).__init__(*args,**kwargs)