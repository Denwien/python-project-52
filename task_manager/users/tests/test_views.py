import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_users_list_available_for_anonymous(client):
    response = client.get(reverse("users"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_users_list_logged_in(client):
    User.objects.create_user(username="user", password="12345")
    client.login(username="user", password="12345")

    response = client.get(reverse("users"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_update_forbidden_for_other_user(client):
    owner = User.objects.create_user(username="owner", password="12345")
    User.objects.create_user(username="other", password="12345")

    client.login(username="other", password="12345")

    response = client.get(reverse("user_update", args=[owner.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_update_allowed_for_self(client):
    user = User.objects.create_user(username="user", password="12345")
    client.login(username="user", password="12345")

    response = client.get(reverse("user_update", args=[user.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_delete_forbidden_for_other_user(client):
    owner = User.objects.create_user(username="owner", password="12345")
    User.objects.create_user(username="other", password="12345")

    client.login(username="other", password="12345")

    response = client.post(reverse("user_delete", args=[owner.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_delete_self(client):
    user = User.objects.create_user(username="user", password="12345")
    client.login(username="user", password="12345")

    response = client.post(reverse("user_delete", args=[user.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="user",
        password="password123",
    )

    client.login(username="user", password="password123")

    response = client.post(reverse("logout"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_user(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="user2",
        password="password123",
    )

    client.login(username="user2", password="password123")

    response = client.post(reverse("user_delete", args=[user.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_user(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="updateuser",
        password="password123",
    )

    client.login(username="updateuser", password="password123")

    response = client.post(
        reverse("user_update", args=[user.id]),
        {
            "first_name": "John",
            "last_name": "Doe",
            "username": "updateuser",
        },
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_other_user_forbidden(client, django_user_model):
    user1 = django_user_model.objects.create_user(
        username="user1",
        password="password123",
    )

    user2 = django_user_model.objects.create_user(
        username="user2",
        password="password123",
    )

    client.login(username="user1", password="password123")

    response = client.post(reverse("user_delete", args=[user2.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_other_user(client):
    user1 = User.objects.create_user(username="u1", password="123")
    user2 = User.objects.create_user(username="u2", password="123")

    client.login(username="u1", password="123")

    response = client.get(reverse("user_update", args=[user2.id]))
    assert response.status_code == 200
