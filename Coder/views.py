from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from .models import Players, Answers, Questions, PlayerScore
from .forms import FormPlayers, FormAnswersPlayer, FormQuestions, SignUpForm, FormEditAccount, FormProfile, FormSearchQuestions, FormSearchPlayers, FormSearchAnswers
from django.db.models import Q, F, FloatField, ExpressionWrapper
from django.db.models.functions import Cast
from django.db.models import DateField, CharField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test

import os
# Create your views here.

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
def index(request):
    params = {}

    return render(request,'index.html',params)

@user_passes_test(is_admin)
def players_view(request):
    params = {}

    if request.method == 'POST':

        form = FormSearchPlayers(request.POST)

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

        ).annotate(date_birth_str=Cast('date_birth', output_field=CharField()),)

        params['form'] = form

        return render(request,'players.html',params)
    
    else:
        
        form = FormSearchPlayers()
        
        params['players'] = Players.objects.all().annotate(date_birth_str=Cast('date_birth', output_field=CharField()),)
        params['form'] = form

    return render(request,'players.html',params)

@login_required
def players_add(request):

    params = {}

    if request.method == 'POST':

        form = FormPlayers(request.POST, request.FILES)

        params['form'] = form
        if form.is_valid():
            _user = form.cleaned_data['user']
            _image = form.cleaned_data['image']
            _first_name = form.cleaned_data['first_name']
            _last_name = form.cleaned_data['last_name']
            _date_birth = form.cleaned_data['date_birth']
            _phone = form.cleaned_data['phone']
            _adress = form.cleaned_data['adress']
            _city = form.cleaned_data['city']
            _state = form.cleaned_data['state']
            _country = form.cleaned_data['country']

            _newPlayer = Players(
                user = _user,
                image = _image,
                first_name = _first_name,
                last_name = _last_name,
                date_birth = _date_birth,
                phone = _phone,
                adress = _adress,
                city = _city,
                state = _state,
                country = _country,
                )

            _newPlayer.save()

            return HttpResponseRedirect('/Coder/players')
        else:
            return render(request,'players_add.html', params)
    
    else:
        form = FormPlayers()
        params['form'] = form
        
        return render(request,'players_add.html', params)


@login_required
def players_edit(request, id):

    params = {}

    _player = Players.objects.get(user__id = id)

    if request.method == 'POST':

        form = FormPlayers(request.POST, request.FILES)
        form.fields['image'].required = False

        print(request.FILES)
        print(bool(request.FILES))
        
        params['form'] = form

        if form.is_valid():
            if request.FILES:
                _player.image.delete()
                _player.image = form.cleaned_data['image']

            _player.first_name = form.cleaned_data['first_name']
            _player.last_name = form.cleaned_data['last_name']
            _player.date_birth = form.cleaned_data['date_birth']
            _player.phone = form.cleaned_data['phone']
            _player.adress = form.cleaned_data['adress']
            _player.city = form.cleaned_data['city']
            _player.state = form.cleaned_data['state']
            _player.country = form.cleaned_data['country']

            _player.save()

            return redirect(reverse('players_view'))
        else:

            return render(request,'players_edit.html', params)
    
    else:
        form = FormPlayers(instance=_player)
        form.fields['image'].required = False
        params['form'] = form
        
        return render(request,'players_edit.html', params)


@login_required
def players_delete(request,id):

    player = Players.objects.get(id=id)
    player = player.delete()
    
    return redirect(reverse('players_view'))

@login_required
def questions_view(request):
    params = {}

    if request.method == 'POST':

        print(request.POST)
        form = FormSearchQuestions(request.POST)

        _title = request.POST['title']
        _category = request.POST['category']
        _date = request.POST['date']
        _author = request.POST['author']       
        _question = request.POST['question']
        _correct_answer = request.POST['correct_answer']
        _status = request.POST['status']

        params['questions'] = Questions.objects.filter(
            title__icontains = _title,
            category__icontains = _category,
            date__icontains = _date,
            author__user__id__icontains = _author,
            question__icontains = _question,
            correct_answer__icontains = _correct_answer,
            status__icontains = _status,
        )

        params['form'] = form

        return render(request,'questions.html',params)
    
    else:
        
        form = FormSearchQuestions()
        
        params['questions'] = Questions.objects.all()
        params['form'] = form

    return render(request,'questions.html',params)

@login_required
def questions_add(request):
    params = {}

    # User sends data to server
    if request.method == 'POST':

        form = FormQuestions(request.POST)

        #Data valid
        if form.is_valid():

            _title = form.cleaned_data['title']
            _category = form.cleaned_data['category']
            _question = form.cleaned_data['question']
            _correct_answer = form.cleaned_data['correct_answer']
            _date = form.cleaned_data['date']
            _author = form.cleaned_data['author']
            _status = form.cleaned_data['status']

            _newQuestion = Questions(
                title = _title,
                category = _category,
                question = _question, 
                correct_answer = _correct_answer,
                date = _date,
                author = _author,
                status = _status,
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

@login_required
def questions_edit(request, id):

    params = {}
    _question = Questions.objects.get(id=id)

    if request.method == 'POST':

        form = FormQuestions(request.POST)
        
        params['form'] = form

        if form.is_valid():
            _question.title = form.cleaned_data['title']
            _question.category = form.cleaned_data['category']
            _question.question = form.cleaned_data['question']
            _question.correct_answer = form.cleaned_data['correct_answer']
            _question.date = form.cleaned_data['date']
            _question.author = form.cleaned_data['author']
            _question.status = form.cleaned_data['status']
            _question.save()

            return redirect(reverse('questions_view'))
        else:

            return render(request,'questions_edit.html', params)
    
    else:
        form = FormQuestions(instance=_question)
        
        params['form'] = form
        
        return render(request,'questions_edit.html', params)

@login_required
def questions_delete(request,id):
    
    question = Questions.objects.get(id=id)
    question = question.delete()
    
    return redirect(reverse('questions_view'))

@login_required
def questions_pending(request,id):
    
    question = Questions.objects.get(id=id)
    question.status = 'pending'
    question.save()
    
    return redirect(reverse('questions_view'))

@login_required
def questions_closed(request,id):
    
    _question = Questions.objects.get(id=id)
    _question.status = 'closed'
    _question.save()

    list_answers = Answers.objects.filter(question=_question)



    
    return redirect(reverse('questions_view'))

@login_required
def questions_open(request,id):
    
    question = Questions.objects.get(id=id)
    question.status = 'open'
    question.save()
    
    return redirect(reverse('questions_view'))

@login_required
def questions_result(request,id):
    params = {}

    _question = Questions.objects.get(id=id)

    _answers = Answers.objects.filter(question=_question).annotate(
        closest=ExpressionWrapper(F('answer') - F('question__correct_answer'), output_field=FloatField())
    ).order_by('-closest')
    
    
    _first_three = _answers[0:3]
    _winner = _answers[0]
    _last_one = _answers.last()

    _podium = list(_first_three) + [_last_one]

    params['winner'] = _winner
    params['first_three'] = _first_three
    params['last_one'] = _last_one
    params['podium'] = _podium


    params['answers'] = _answers


    
    return render(request,'questions_result.html',params)


@login_required
def answers_view(request):
    params = {}

    if request.method == 'POST':

        form = FormSearchAnswers(request.POST)

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
        
        form = FormSearchAnswers()
        
        params['answers'] = Answers.objects.all()
        params['form'] = form

    return render(request,'answers.html',params)

@login_required
def answersPlayer_add(request):
    params = {}
    open_questions = Questions.objects.filter(status = 'open' ) 

    # User sends data to server
    if request.method == 'POST':


        form = FormAnswersPlayer(request.POST,open_questions=open_questions)

        #Data valid
        if form.is_valid():

            _question = form.cleaned_data['question']
            _answer = form.cleaned_data['answer']
            _player = Players.objects.get(user=request.user)

            _newAnswer = Answers(question = _question, 
                                 answer = _answer, 
                                 player = _player,
                                )

            _newAnswer.save()

            return HttpResponseRedirect('/Coder/answers')

        
        #Data no valid
        else:
            params['form'] = form

            return render(request,'answersPlayer_add.html',params)


    # User asks data to server
    else:
        
        form = FormAnswersPlayer(open_questions=open_questions)
        
        params['form'] = form

        return render(request,'answersPlayer_add.html',params)

def signin(request):
    
    if request.method == 'POST':
        
        params = {}

        form = AuthenticationForm(request, data = request.POST)

        params['form'] = form

        if form.is_valid():

            _data = form.cleaned_data
            
            _username = _data['username']

            _password = _data['password']

            _user = authenticate(username=_username, password = _password)

            if _user is not None:

                login(request,_user)
                
                return redirect(reverse('index'))

            else:
                
                params['message'] = 'User or password incorrect.'

                return render(request, 'signin.html',params)
        
        else:
            params['message'] = 'User or password incorrect.'

            return render(request, 'signin.html',params)
        
    else:
        
        params = {}
        
        form = AuthenticationForm()
        
        params['form'] = form

        return render(request,'signin.html', params)

def signup(request):

    if request.method == 'POST':
        
        params = {}

        form = SignUpForm(request.POST)

        params['form'] = form


        if form.is_valid():

            params['signup'] = True

            form.save()

            return render(request, 'index.html', params)

        
        else:

            return render(request, 'signup.html',params)
        
    else:
        
        params = {}
        
        form = SignUpForm()
        
        params['form'] = form

        return render(request,'signup.html', params)
    
@login_required
def editAccount(request):

    params = {}
    user = request.user

    if request.method == 'POST':
        
        form = FormEditAccount(request.POST)

        if form.is_valid():
            
            _user = form.cleaned_data
            
            user.email = _user['email']

            user.password1 = _user['password1']

            user.password2 = _user['password2']

            user.save()

            return redirect(reverse('index'))

        else:

            return render(request,'editAccount.html', params)
            
    
    else:
        form = FormEditAccount(instance=user)
        
        params['form'] = form
        
        return render(request,'editAccount.html', params)

@login_required
def editProfile(request):
    params = {}

    _player = Players.objects.get(user = request.user)

    if request.method == 'POST':

        form = FormProfile(request.POST, request.FILES)
        form.fields['image'].required = False

        params['form'] = form

        if form.is_valid():
            if request.FILES:
                _player.image.delete()
                _player.image = form.cleaned_data['image']

            _player.first_name = form.cleaned_data['first_name']
            _player.last_name = form.cleaned_data['last_name']
            _player.date_birth = form.cleaned_data['date_birth']
            _player.phone = form.cleaned_data['phone']
            _player.adress = form.cleaned_data['adress']
            _player.city = form.cleaned_data['city']
            _player.state = form.cleaned_data['state']
            _player.country = form.cleaned_data['country']

            _player.save()

            return redirect(reverse('index'))
        else:

            return render(request,'editProfile.html', params)
    
    else:
        form = FormProfile(instance=_player)
        form.fields['image'].required = False
        params['form'] = form
        
        return render(request,'editProfile.html', params)
