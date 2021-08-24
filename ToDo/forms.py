from django.forms import ModelForm, DateTimeInput, HiddenInput, TextInput, Textarea
from .models import TodoList


class TodoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ["title", "description", "deadline"]
        widgets = {
            "deadline": DateTimeInput(attrs={
                "type": "date",
                "class": 'todo-date'
            }),
            "title": TextInput(attrs={
                "class": "todo-title",
                "placeholder": "The name of the task"
            }),
            "description": Textarea(attrs={
                "class": "todo-description",
                "placeholder": "My Task"
            })
        }
