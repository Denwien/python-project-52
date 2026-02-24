import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_users_list_requires_login(client):
    response = client.get(reverse("users"))
    assert response.status_code == 302  # redirect to login


@pytest.mark.django_db
def test_users_list_logged_in(client):
    user = User.objects.create_user(username="user", password="12345")
    client.login(username="user", password="12345")

    response = client.get(reverse("users"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_update_forbidden_for_other_user(client):
    owner = User.objects.create_user(username="owner", password="12345")
    other = User.objects.create_user(username="other", password="12345")

    client.login(username="other", password="12345")

    response = client.get(reverse("user_update", args=[owner.id]))
    assert response.status_code == 302  # redirect with error


@pytest.mark.django_db
def test_user_update_allowed_for_self(client):
    user = User.objects.create_user(username="user", password="12345")
    client.login(username="user", password="12345")

    response = client.get(reverse("user_update", args=[user.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_delete_forbidden_for_other_user(client):
    owner = User.objects.create_user(username="owner", password="12345")
    other = User.objects.create_user(username="other", password="12345")

    client.login(username="other", password="12345")

    response = client.post(reverse("user_delete", args=[owner.id]))
    assert response.status_code == 302


@pytest.mark.django_db
def test_user_delete_self(client):
    user = User.objects.create_user(username="user", password="12345")
    client.login(username="user", password="12345")

    response = client.post(reverse("user_delete", args=[user.id]))
    assert response.status_code == 302
    assert not User.objects.filter(id=user.id).exists()