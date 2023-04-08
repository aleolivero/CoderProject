from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Coder import views

urlpatterns = [
    path('', views.index, name='index'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)