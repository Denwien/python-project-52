from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    StatusCreateView,
    StatusDeleteView,
    StatusListView,
    StatusUpdateView,
    LabelListView,
    LabelCreateView,
    LabelUpdateView,
    LabelDeleteView,
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskListView,
    TaskUpdateView,
    index,
)

urlpatterns = [
    path("labels/", LabelListView.as_view(), name="labels"),
    path("labels/create/", LabelCreateView.as_view(), name="label_create"),
    path(
        "labels/<int:pk>/update/",
        LabelUpdateView.as_view(),
        name="label_update"
    ),
    path(
        "labels/<int:pk>/delete/",
        LabelDeleteView.as_view(),
        name="label_delete"
    ),
    path("", index, name="index"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="auth/login.html",
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path(
        "statuses/",
        StatusListView.as_view(),
        name="statuses",
    ),
    path(
        "statuses/create/",
        StatusCreateView.as_view(),
        name="status_create",
    ),
    path(
        "statuses/<int:pk>/update/",
        StatusUpdateView.as_view(),
        name="status_update",
    ),
    path(
        "statuses/<int:pk>/delete/",
        StatusDeleteView.as_view(),
        name="status_delete",
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="tasks",
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task_create",
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task_update",
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task_delete",
    ),
    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task_detail",
    ),
]
