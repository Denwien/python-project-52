from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from .forms import UserCreateForm, UserUpdateForm, UserLoginForm


class UserListView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "users/create.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/update.html"
    success_url = reverse_lazy("users")

    def test_func(self):
        return self.get_object() == self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно изменён")
        return super().form_valid(form)


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users")

    def test_func(self):
        user = self.get_object()
        if user.authored_tasks.exists() or user.executed_tasks.exists():
            messages.error(self.request, "Невозможно удалить пользователя, потому что он используется")
            return False
        return user == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Пользователь успешно удалён")
        return super().delete(request, *args, **kwargs)


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = "auth/login.html"
    success_message = "Вы залогинены"
    
    def get_success_url(self):
        return reverse_lazy("index")
