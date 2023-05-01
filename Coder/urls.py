from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Coder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),

    path('players/', views.players_view, name='players_view'),
    path('playersAdd/', views.players_add, name='players_add'),
    path('playersEdit/<id>', views.players_edit, name='players_edit'),
    path('playersDelete/<id>', views.players_delete, name='players_delete'),

    
    path('answers/', views.answers_view, name='answers_view'),
    path('answersPlayerAdd/', views.answersPlayer_add, name='answersPlayerAdd'),
    path('answersPlayerView/', views.answersPlayer_view, name='answersPlayerView'),

    path('eventsPlayerView/', views.eventsPlayer_view, name='eventsPlayerView'),


    path('questions/', views.questions_view, name='questions_view'),
    path('questionsAdd/', views.questions_add, name='questions_add'),
    path('questionsEdit/<id>', views.questions_edit, name='questions_edit'),
    path('questionsDelete/<id>', views.questions_delete, name='questions_delete'),
    path('questionsDetermined/<id>', views.questions_determined, name='questions_determined'),
    path('questionsUndetermined/<id>', views.questions_undetermined, name='questions_undetermined'),

    path('questionsClosed/<id>', views.questions_closed, name='questions_closed'),
    path('questionsOpen/<id>', views.questions_open, name='questions_open'),
    path('questionsResult/<id>', views.questions_result, name='questions_result'),


    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('editAccount/', views.editAccount, name='editAccount'),
    path('editProfile/', views.editProfile, name='editProfile'),





] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)