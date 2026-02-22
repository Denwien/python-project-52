from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import Task

User = get_user_model()


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']
        labels = {
            'name': _('Имя'),
            'description': _('Описание'),
            'status': _('Статус'),
            'executor': _('Исполнитель'),
            'labels': _('Метки'),
        }
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'executor': forms.Select(attrs={'class': 'form-control'}),
            'labels': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['executor'].queryset = (
            User.objects.all().order_by('username')
        )
        self.fields['executor'].required = False
        self.fields['executor'].empty_label = "---------"
        
        # Use full name for display in select options
        def label_from_instance(obj):
            return obj.get_full_name() or obj.username
        
        self.fields['executor'].label_from_instance = label_from_instance
