import os
import pytest
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_status(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="testuser",
        password=os.getenv("TEST_PASSWORD", "testpass"),
    )

    client.login(username="testuser", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.post(
        reverse("status_create"),
        {"name": "New Status"},
    )

    assert response.status_code == 302

@pytest.mark.django_db
def test_status_delete_when_used(client):
    from django.urls import reverse
    from django.contrib.auth.models import User
    from task_manager.statuses.models import Status
    from task_manager.tasks.models import Task

    user = User.objects.create_user(username="user", password=os.getenv("TEST_PASSWORD", "testpass"))
    client.login(username="user", password=os.getenv("TEST_PASSWORD", "testpass"))

    status = Status.objects.create(name="new")

    Task.objects.create(
        name="task",
        status=status,
        author=user
    )

    response = client.post(reverse("status_delete", args=[status.id]))

    assert response.status_code == 302
