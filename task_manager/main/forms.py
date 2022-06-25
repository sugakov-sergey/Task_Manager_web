from .models import Task, Purpose
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "body", "status"]
        widgets = {"title": TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Введите значение'}),
                   "body": Textarea(attrs={'class': 'form-control',
                                             'placeholder': 'Введите описание'}),
                   "status": TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Введите статус'}),
                   }

class PurposeForm(ModelForm):
    class Meta:
        model = Purpose
        fields = ["title", "body", "rank"]