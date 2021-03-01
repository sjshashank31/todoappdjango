from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'due_date']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'due_date', 'priority', 'completed']
