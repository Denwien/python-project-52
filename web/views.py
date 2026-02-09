from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Status, Task, Label


def index(request):
    return render(request, "index.html")


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/index.html"
    context_object_name = "statuses"


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    fields = ["name"]
    template_name = "statuses/create.html"
    success_url = reverse_lazy("statuses")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Status created successfully",
        )
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    fields = ["name"]
    template_name = "statuses/update.html"
    success_url = reverse_lazy("statuses")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Status updated successfully",
        )
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = "statuses/delete.html"
    success_url = reverse_lazy("statuses")

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            "Status deleted successfully",
        )
        return super().delete(request, *args, **kwargs)


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["name", "description", "status", "executor"]
    template_name = "tasks/create.html"
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(
            self.request,
            "Task created successfully",
        )
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["name", "description", "status", "executor"]
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Task updated successfully",
        )
        return super().form_valid(form)


class TaskDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks")

    def test_func(self):
        return self.get_object().author == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            "Task deleted successfully",
        )
        return super().delete(request, *args, **kwargs)


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/index.html"
    context_object_name = "labels"


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    fields = ["name"]
    template_name = "labels/create.html"
    success_url = reverse_lazy("labels")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Label created successfully",
        )
        return super().form_valid(form)


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    fields = ["name"]
    template_name = "labels/update.html"
    success_url = reverse_lazy("labels")

    def form_valid(self, form):
        messages.success(
            self.request,
            "Label updated successfully",
        )
        return super().form_valid(form)


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = "labels/delete.html"
    success_url = reverse_lazy("labels")

    def delete(self, request, *args, **kwargs):
        label = self.get_object()
        if label.tasks.exists():
            messages.error(
                request,
                "Cannot delete label with tasks",
            )
            return redirect("labels")
        messages.success(
            request,
            "Label deleted successfully",
        )
        return super().delete(request, *args, **kwargs)
