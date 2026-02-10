import django_filters
from django import forms

from .models import Task, Status, Label


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label="Status",
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=Task._meta.get_field("executor").remote_field.model.objects.all(),
        label="Executor",
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label="Label",
    )
    self_tasks = django_filters.BooleanFilter(
        method="filter_self_tasks",
        widget=forms.CheckboxInput(),
        label="Only my tasks",
    )

    class Meta:
        model = Task
        fields = ["status", "executor", "labels"]

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
