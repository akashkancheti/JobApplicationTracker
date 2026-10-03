from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model=JobApplication
        fields=[
            'company',
            'role',
            'status',
            'date_applied',
            'job_link',
            'notes',
           ]
        widgets = {
            'date_applied':forms.DateInput(attrs={'type': 'date'}),
        }