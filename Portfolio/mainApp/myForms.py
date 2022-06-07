from django import forms
from django.forms import ModelForm
from .models import contactFormSubmission

class contactForm(ModelForm):
    class Meta:
        model = contactFormSubmission
        fields = ['firstName', 'lastName', 'email', 'Subject', 'Body']
        labels = {
           'firstName' : '',
           'lastName' : '',
           'email' : '',
           'Subject' : '',
           'Body' : '',
        }
        widgets = {
            'firstName':forms.TextInput(attrs={
            'class': 'input-field col s5',
            'style': 'color: white; margin-bottom: 30px; margin-right: 5px; margin-left: 77.5px',
            'placeholder': 'First Name'}),

            'lastName':forms.TextInput(attrs={
            'class': 'input-field col s5',
            'style': 'color: white;margin-bottom: 30px;',
            'placeholder': 'Last Name'}),

            'email':forms.EmailInput(attrs={
            'class': 'input-field col s10',
            'style': 'color: white; margin-bottom: 30px; margin-left: 80px',
            'placeholder': 'Email'}),

            'Subject':forms.TextInput(attrs={
            'class': 'input-field col s10',
            'style': 'color: white; margin-bottom: 50px; margin-left: 80px',
            'placeholder': 'Subject'}),

            'Body': forms.Textarea(attrs={
            'style': 'color: white; margin-bottom: 50px; width: 83.5%; margin-left: 4px',
            'class': 'materialize-textarea',
            'placeholder': 'Message'})
        }