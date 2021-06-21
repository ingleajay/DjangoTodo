from django import forms
from .models import AddTask

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = ['Task','Date','Time']
        widgets = {
            'Task': forms.TextInput(
                attrs={'placeholder': 'Add Your Task ', 'class': 'form-control'}),
            'Date': forms.DateInput(
                attrs={'placeholder': 'Add Task Completion Date ', 'class': 'form-control', 'type': 'date'}),
            'Time': forms.DateInput(
                attrs={'placeholder': 'Add Task Completion Time', 'class': 'form-control','type':'time'})
        }