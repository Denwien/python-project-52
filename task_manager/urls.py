from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from task_manager.users.views import UserLoginView

urlpatterns = [
    path("", include("task_manager.tasks.urls")),
    path("users/", include("task_manager.users.urls")),
    path("statuses/", include("task_manager.statuses.urls")),
    path("labels/", include("task_manager.labels.urls")),
    path(
        "login/",
        UserLoginView.as_view(
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path("admin/", admin.site.urls),
]
