from django import forms
from .models import Worker


class WorkerForm(forms.ModelForm):
    class Meta:
        widgets = {
            'experience': forms.widgets.DateInput(attrs={'type': 'date'}),
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }

class WorkerCreate(WorkerForm):
    class Meta: 
        model = Worker 
        fields = ['name',
        'birth_date'] 

