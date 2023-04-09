from django.shortcuts import render, HttpResponseRedirect
from .models import Players, Answers, Questions
from .forms import FormPlayers
# Create your views here.

def index(request):
    params = {}

    return render(request,'index.html',params)

def players_view(request):
    params = {}
    params['players'] = Players.objects.all()

    return render(request,'players.html',params)

def players_add(request):
    params = {}

    # User sends data to server
    if request.method == 'POST':

        form = FormPlayers(request.POST)

        #Data valid
        if form.is_valid():

            _first_name = form.cleaned_data['first_name']
            _last_name = form.cleaned_data['last_name']
            _date_birth = form.cleaned_data['date_birth']
            _phone = form.cleaned_data['phone']
            _adress = form.cleaned_data['adress'] 
            _city = form.cleaned_data['city']
            _state = form.cleaned_data['state']
            _country = form.cleaned_data['country']
            _dni = form.cleaned_data['dni']

            _newPlayer = Players(first_name = _first_name, 
                                 last_name = _last_name, 
                                 date_birth = _date_birth,
                                 phone = _phone,
                                 adress = _adress,
                                 city = _city,
                                 state = _state,
                                 country = _country,
                                 dni = _dni,                              
                                )

            _newPlayer.save()

            return HttpResponseRedirect('/Coder/players')

        
        #Data no valid
        else:
            params['form'] = form

            return render(request,'players_add.html',params)


    # User asks data to server
    else:
        
        form = FormPlayers()
        
        params['form'] = form

        return render(request,'players_add.html',params)



def players_search(request):
    params = {}

    return render(request,'players.html',params)

def questions_view(request):
    params = {}
    params['questions'] = Questions.objects.all()

    return render(request,'questions.html',params)

def questions_add(request):
    params = {}
    params['questions'] = Questions.objects.all()

    return render(request,'questions.html',params)

def questions_search(request):
    params = {}
    params['questions'] = Questions.objects.all()

    return render(request,'questions.html',params)

def answers_view(request):
    params = {}
    params['answers'] = Answers.objects.all()

    return render(request,'answers.html',params)

def answers_add(request):
    params = {}
    params['answers'] = Answers.objects.all()

    return render(request,'answers.html',params)

def answers_search(request):
    params = {}
    params['answers'] = Answers.objects.all()

    return render(request,'answers.html',params)
