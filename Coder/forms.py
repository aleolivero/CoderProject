from django import forms
from django.forms import ModelForm
from Coder.models import Players, Questions, Answers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormPlayers(ModelForm):
    class Meta:
        model = Players
        fields = [
            'user',
            'image',
            'first_name', 
            'last_name', 
            'date_birth' ,
            'phone',
            'adress', 
            'city',
            'state', 
            'country', 
        ]
        widgets = {
            'date_birth': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(FormPlayers, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class FormSearchPlayers(ModelForm):
    class Meta:
        model = Players
        fields = [
            'user',
            'image',
            'first_name', 
            'last_name', 
            'date_birth' ,
            'phone',
            'adress', 
            'city',
            'state', 
            'country', 
        ]
        widgets = {
            'date_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(FormSearchPlayers, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

class FormQuestions(ModelForm):
    class Meta:
        model = Questions
        fields = [
            'title',
            'category',
            'question', 
            'date',
            'correct_answer', 
            'author',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class FormSearchQuestions(ModelForm):
    class Meta:
        model = Questions
        fields = [
            'title',
            'category',
            'question', 
            'date',
            'correct_answer', 
            'author',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(FormSearchQuestions, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False


class FormAnswers(ModelForm):
    class Meta:
        model = Answers
        fields = [
            'question', 
            'answer',
            'player', 
        ]
        widgets = {
            'question': forms.Select(attrs={'class': 'form-control'}),
            'player': forms.Select(attrs={'class': 'form-control'}),
            'answer': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class FormEditAccount(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','password1','password2']

class FormProfile(ModelForm):
    class Meta:
        model = Players
        fields = [
            'image',
            'first_name', 
            'last_name', 
            'date_birth' ,
            'phone',
            'adress', 
            'city',
            'state', 
            'country', 
        ]
        widgets = {
            'date_birth': forms.DateInput(attrs={'type': 'date'}),
        }
