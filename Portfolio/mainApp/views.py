from django.shortcuts import render
from .models import Label, Project, ContactFormSubmission
from datetime import datetime
from django.core.mail import send_mail
def index(request):
    request.session['messageSent'] = False
    if request.method == 'POST':
        request.session['messageSent'] = True
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        email = request.POST['email']
        Subject = request.POST['subject']
        Body = request.POST['body']
        userMessages = ContactFormSubmission(firstName = firstName, lastName = lastName, email = email, Subject = Subject, Body = Body, time = datetime.now())
        userMessages.save()

    messageSent = request.session.get('messageSent')
    context = {"projects":Project.objects.all, "messageSent":messageSent}
    return render(request, 'mainApp/index.html', context=context)


def privacy(request):

    return render(request, 'mainApp/privacy.html')


def terms(request):

    return render(request, 'mainApp/terms.html')


def license(request):

    return render(request, 'mainApp/license.html')


def credits(request):

    return render(request, 'mainApp/credits.html')