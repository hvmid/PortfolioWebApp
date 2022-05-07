from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('about', views.about, name='about'),
]

urlpatterns += [
    path('contact', views.contact, name='contact'),
]

urlpatterns += [
    path('projects', views.projects, name='projects'),
]