import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_create_status(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="testuser",
        password="password123",
    )

    client.login(username="testuser", password="password123")

    response = client.post(
        reverse("status_create"),
        {"name": "New Status"},
    )

    assert response.status_code == 302
