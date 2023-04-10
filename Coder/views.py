from django.shortcuts import render, HttpResponseRedirect
from .models import Players, Answers, Questions
from .forms import FormPlayers, FormAnswers, FormQuestions
from django.db.models import Q

# Create your views here.

def index(request):
    params = {}

    return render(request,'index.html',params)

def players_view(request):
    params = {}

    if request.method == 'POST':

        form = FormPlayers(request.POST)

        _first_name = request.POST['first_name']
        _last_name = request.POST['last_name']
        _date_birth = request.POST['date_birth']
        _phone = request.POST['phone']
        _adress = request.POST['adress'] 
        _city = request.POST['city']
        _state = request.POST['state']
        _country = request.POST['country']

        params['players'] = Players.objects.filter(
            first_name__icontains = _first_name,
            last_name__icontains = _last_name,
            date_birth__icontains = _date_birth,
            phone__icontains = _phone,
            adress__icontains = _adress,
            city__icontains = _city,
            state__icontains = _state,
            country__icontains = _country,

        )

        params['form'] = form

        return render(request,'players.html',params)
    
    else:
        
        form = FormPlayers()
        
        params['players'] = Players.objects.all()
        params['form'] = form

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

def questions_view(request):
    params = {}

    if request.method == 'POST':

        form = FormQuestions(request.POST)

        _question = request.POST['question']
        _correct_answer = request.POST['correct_answer']

        params['questions'] = Questions.objects.filter(
            question__icontains = _question,
            correct_answer__icontains = _correct_answer,
        )

        params['form'] = form

        return render(request,'questions.html',params)
    
    else:
        
        form = FormQuestions()
        
        params['questions'] = Questions.objects.all()
        params['form'] = form

    return render(request,'questions.html',params)

def questions_add(request):
    params = {}

    # User sends data to server
    if request.method == 'POST':

        form = FormQuestions(request.POST)

        #Data valid
        if form.is_valid():

            _question = form.cleaned_data['question']
            _correct_answer = form.cleaned_data['correct_answer']

            _newQuestion = Questions(question = _question, 
                                 correct_answer = _correct_answer, 
                                )

            _newQuestion.save()

            return HttpResponseRedirect('/Coder/questions')

        
        #Data no valid
        else:
            params['form'] = form

            return render(request,'questions_add.html',params)


    # User asks data to server
    else:
        
        form = FormQuestions()
        
        params['form'] = form

        return render(request,'questions_add.html',params)

def answers_view(request):
    params = {}

    if request.method == 'POST':

        form = FormAnswers(request.POST)

        _question = request.POST['question']
        _answer = request.POST['answer']
        _player = request.POST['player']

        params['answers'] = Answers.objects.filter(
           Q(player__first_name__icontains = _player) | Q(player__last_name__icontains = _player) ,
           answer__icontains = _answer,
           question__question__icontains = _question
        )

        params['form'] = form

        return render(request,'answers.html',params)
    
    else:
        
        form = FormAnswers()
        
        params['answers'] = Answers.objects.all()
        params['form'] = form

    return render(request,'answers.html',params)

def answers_add(request):
    params = {}

    # User sends data to server
    if request.method == 'POST':

        form = FormAnswers(request.POST)

        #Data valid
        if form.is_valid():

            _question = form.cleaned_data['question']
            _answer = form.cleaned_data['answer']
            _player = form.cleaned_data['player']

            _newAnswer = Answers(question = _question, 
                                 answer = _answer, 
                                 player = _player,
                                )

            _newAnswer.save()

            return HttpResponseRedirect('/Coder/answers')

        
        #Data no valid
        else:
            params['form'] = form

            return render(request,'answers_add.html',params)


    # User asks data to server
    else:
        
        form = FormAnswers()
        
        params['form'] = form

        return render(request,'answers_add.html',params)

