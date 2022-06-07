from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Project(models.Model):

    # Fields
    name = models.CharField(max_length=100, help_text='Project Name')
    summary = models.TextField(max_length=1000, help_text='Project Summary')
    github = models.URLField(max_length=300, help_text='Project Github')
    Image = models.ImageField(upload_to='media/projectImages/')

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Blog(models.Model):

    # Fields
    title = models.CharField(max_length=100, help_text='Blog Title')
    content = models.TextField()
    slug = models.CharField(max_length=200, default=1)
    image = models.ImageField(upload_to='media/projectImages/')
    published = models.DateTimeField(auto_now_add=True)
    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.title

class Skill(models.Model):

    # Fields
    name = models.CharField(max_length=100, help_text='Project Name')
    Image = models.FileField(upload_to="")

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class projectSkill(models.Model):

    # Fields
    skillName = models.CharField(max_length=100, help_text='Skill Name')
    projectName = models.CharField(max_length=100, help_text='Project Name')

    def __str__(self):
        return self.name

class contactFormSubmission(models.Model):

    # Fields
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.firstName

