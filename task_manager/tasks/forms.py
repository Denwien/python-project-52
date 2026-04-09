from django import forms
from django.contrib.auth.models import User

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
