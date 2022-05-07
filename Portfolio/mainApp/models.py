from django.db import models
from django.urls import reverse

class Label(models.Model):

    # Fields
    name = models.CharField(max_length=100, help_text='Label Name')
    description = models.CharField(max_length=100, help_text='Label Description')

    def __str__(self):
        return self.name

class Project(models.Model):

    # Fields
    name = models.CharField(max_length=100, help_text='Project Name')
    summary = models.CharField(max_length=1000, help_text='Project Summary')
    github = models.CharField(max_length=300, help_text='Project Github')

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class projectLabel(models.Model):

    # Fields
    labelName = models.CharField(max_length=100, help_text='Label Name')
    projectName = models.CharField(max_length=100, help_text='Project Name')

    def __str__(self):
        return self.name

class ContactFormSubmission(models.Model):

    # Fields
    firstName = models.CharField(max_length=100, help_text='First Name')
    lastName = models.CharField(max_length=1000, help_text='Last Name')
    Subject = models.CharField(max_length=300, help_text='Subject')
    Body = models.CharField(max_length=1000, help_text='Body')

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name