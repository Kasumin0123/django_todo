from django import forms
from django.forms import ModelForm

from .models import Todo

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "list", "dueDate", "dueTime"]
        widgets = {
            'dueDate': DateInput(),
            'dueTime': TimeInput(),
        }