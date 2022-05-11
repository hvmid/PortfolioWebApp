from django.urls import path, include
from . import views

app_name = "mainApp"
urlpatterns = [
    path('', views.index, name='index'),
    path('privacy.html', views.privacy, name='privacy'),
    path('terms.html', views.terms, name='terms'),
    path('license.html', views.license, name='license'),
    path('credits.html', views.credits, name='credits'),
]


