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
    path('answersAdd/', views.answers_add, name='answers_add'),

    path('questions/', views.questions_view, name='questions_view'),
    path('questionsAdd/', views.questions_add, name='questions_add'),

    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', LogoutView.as_view(), name='signout'),





] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)