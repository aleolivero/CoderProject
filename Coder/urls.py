from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Coder import views

urlpatterns = [
    path('', views.index, name='index'),

    path('players', views.players_view, name='players_view'),
    path('playersAdd', views.players_add, name='players_add'),
    path('playersSearch', views.players_search, name='players_search'),
    
    path('answers', views.answers_view, name='answers_view'),
    path('answersAdd', views.answers_add, name='answers_add'),
    path('answersSearch', views.answers_search, name='answers_search'),

    path('questions', views.questions_view, name='questions_view'),
    path('questionsAdd', views.questions_add, name='questions_add'),
    path('questionsSearch', views.questions_search, name='questions_search'),



] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)