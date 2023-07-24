from django import forms
from django.forms import ModelForm
from .models import List

from .models import Todo


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ('name',)
        labels = {'name': '名前'}


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "list", "dueDate", "dueTime"]
        labels = {
            'title': '名前',
            'description': '詳細',
            'list': 'リスト',
            'dueDate': '日付',
            'dueTime': '時刻'
        }
        widgets = {
            'dueDate': DateInput(),
            'dueTime': TimeInput(),
        }
