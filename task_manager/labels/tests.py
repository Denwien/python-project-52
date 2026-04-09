import pytest
import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_label(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="testuser",
        password="test_password",
    )

    client.login(username="testuser", password="test_password")

    response = client.post(
        reverse("label_create"),
        {"name": "New Label"},
    )

    assert response.status_code == 302

@pytest.mark.django_db
def test_label_delete_when_used(client):
    from django.urls import reverse
    from django.contrib.auth.models import User
    from task_manager.labels.models import Label
    from task_manager.statuses.models import Status
    from task_manager.tasks.models import Task

    user = User.objects.create_user(username="user", password="test_password")
    client.login(username="user", password="test_password")

    status = Status.objects.create(name="new")
    label = Label.objects.create(name="bug")

    task = Task.objects.create(
        name="task",
        status=status,
        author=user,
    )
    task.labels.add(label)

    response = client.post(reverse("label_delete", args=[label.id]))

    assert response.status_code == 302
