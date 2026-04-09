from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Task


class FullNameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        full_name = f"{obj.first_name} {obj.last_name}".strip()
        return full_name if full_name else obj.username


class TaskForm(forms.ModelForm):
    executor = FullNameChoiceField(
        queryset=User.objects.all(),
        required=False,
        label="Исполнитель",
    )

    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]
        labels = {
            "name": "Имя",
            "description": "Описание",
            "status": "Статус",
            "labels": "Метки",
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if name and Task.objects.filter(name=name).exists():
            raise ValidationError("Задача с таким именем уже существует")

        return name
