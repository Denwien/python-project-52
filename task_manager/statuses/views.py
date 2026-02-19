from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from .models import Status


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
        messages.success(self.request, "Status created successfully")
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    fields = ["name"]
    template_name = "statuses/update.html"
    success_url = reverse_lazy("statuses")

    def form_valid(self, form):
        messages.success(self.request, "Status updated successfully")
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = "statuses/delete.html"
    success_url = reverse_lazy("statuses")

    def delete(self, request, *args, **kwargs):
        status = self.get_object()
        if status.tasks.exists():
            messages.error(request, "Cannot delete status with tasks")
            return redirect("statuses")
        messages.success(request, "Status deleted successfully")
        return super().delete(request, *args, **kwargs)
