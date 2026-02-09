from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    StatusCreateView,
    StatusDeleteView,
    StatusListView,
    StatusUpdateView,
    index,
)

urlpatterns = [
    path('', index, name='index'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='auth/login.html',
        ),
        name='login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout',
    ),
    path(
        'statuses/',
        StatusListView.as_view(),
        name='statuses',
    ),
    path(
        'statuses/create/',
        StatusCreateView.as_view(),
        name='status_create',
    ),
    path(
        'statuses/<int:pk>/update/',
        StatusUpdateView.as_view(),
        name='status_update',
    ),
    path(
        'statuses/<int:pk>/delete/',
        StatusDeleteView.as_view(),
        name='status_delete',
    ),
]
