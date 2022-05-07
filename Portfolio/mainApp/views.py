from django.shortcuts import render
from .models import Label, Project

def index(request):

    context = {"projects":Project.objects.all}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'mainApp/index.html', context=context)

def projects(request):

    context = {"projects":Project.objects.all}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'mainApp/projects.html', context=context)

def about(request):

    return render(request, 'mainApp/about.html')

def contact(request):

    return render(request, 'mainApp/contact.html')