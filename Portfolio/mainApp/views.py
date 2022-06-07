from django.shortcuts import render
from .models import Project, contactFormSubmission, Skill, Blog
from datetime import datetime
from django.core.mail import send_mail
from .myForms import contactForm

def index(request):

    form = contactForm()
    if request.method == 'POST':
        request.session['messageSent'] = True
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            form = contactForm()

    messageSent = request.session.get('messageSent', False)
    context = {"projects":Project.objects.all, "messageSent":messageSent, "skills":Skill.objects.all, "form": form, "blogs":Blog.objects.all}
    return render(request, 'mainApp/index.html', context=context)


def privacy(request):

    return render(request, 'mainApp/privacy.html')


def terms(request):

    return render(request, 'mainApp/terms.html')


def license(request):

    return render(request, 'mainApp/license.html')


def credits(request):

    return render(request, 'mainApp/credits.html')


# def single_slug(request, single_slug):
#     categories = [c.category_slug for c in TutorialCategory.objects.all()]
#     if single_slug in categories:
#       return HttpResponse(f"{single_slug} is a category")

#     tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
#     if single_slug in tutorials:
#       return HttpResponse(f"{single_slug} is a Tutorial")

#     return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")


