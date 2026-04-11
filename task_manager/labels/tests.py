import os

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_label(client, django_user_model):
    django_user_model.objects.create_user(
        username="testuser",
        password=os.getenv(
            "TEST_PASSWORD",
            "testpass",
        ),
    )

    client.login(
        username="testuser",
        password=os.getenv(
            "TEST_PASSWORD",
            "testpass",
        ),
    )

    response = client.post(
        reverse("label_create"),
        {"name": "New Label"},
    )

    assert response.status_code == 302


@pytest.mark.django_db
def test_label_delete_when_used(client):
    from django.contrib.auth.models import User
    from django.urls import reverse

    from task_manager.labels.models import Label
    from task_manager.statuses.models import Status
    from task_manager.tasks.models import Task

    user = User.objects.create_user(
        username="user",
        password=os.getenv(
            "TEST_PASSWORD",
            "testpass",
        ),
    )
    client.login(
        username="user",
        password=os.getenv(
            "TEST_PASSWORD",
            "testpass",
        ),
    )

    status = Status.objects.create(name="new")
    label = Label.objects.create(name="bug")

    task = Task.objects.create(
        name="task",
        status=status,
        author=user,
    )
    task.labels.add(label)

    response = client.post(
        reverse(
            "label_delete",
            args=[label.id],
        )
    )

    assert response.status_code == 302
