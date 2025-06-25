from django import forms
from .models import Task

class task_appForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'