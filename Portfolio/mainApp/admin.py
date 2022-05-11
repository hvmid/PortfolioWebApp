from django.contrib import admin
from .models import Language, Label, Project, projectLabel, ContactFormSubmission, skill


admin.site.register(Language)
admin.site.register(Label)
admin.site.register(Project)
admin.site.register(projectLabel)
admin.site.register(ContactFormSubmission)
admin.site.register(skill)
