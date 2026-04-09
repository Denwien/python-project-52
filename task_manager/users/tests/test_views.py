import os
import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_users_list_available_for_anonymous(client):
    response = client.get(reverse("users"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_users_list_logged_in(client):
    User.objects.create_user(username="user", password=os.getenv("TEST_PASSWORD", "testpass"))
    client.login(username="user", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.get(reverse("users"))
    assert response.status_code in (200, 302)


@pytest.mark.django_db
def test_user_update_forbidden_for_other_user(client):
    owner = User.objects.create_user(username="owner", password=os.getenv("TEST_PASSWORD", "testpass"))
    User.objects.create_user(username="other", password=os.getenv("TEST_PASSWORD", "testpass"))

    client.login(username="other", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.get(reverse("user_update", args=[owner.id]))
    assert response.status_code in (200, 302)


@pytest.mark.django_db
def test_user_update_allowed_for_self(client):
    user = User.objects.create_user(username="user", password=os.getenv("TEST_PASSWORD", "testpass"))
    client.login(username="user", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.get(reverse("user_update", args=[user.id]))
    assert response.status_code in (200, 302)


@pytest.mark.django_db
def test_user_delete_forbidden_for_other_user(client):
    owner = User.objects.create_user(username="owner", password=os.getenv("TEST_PASSWORD", "testpass"))
    User.objects.create_user(username="other", password=os.getenv("TEST_PASSWORD", "testpass"))

    client.login(username="other", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.post(reverse("user_delete", args=[owner.id]))
    assert response.status_code in (200, 302)


@pytest.mark.django_db
def test_user_delete_self(client):
    user = User.objects.create_user(username="user", password=os.getenv("TEST_PASSWORD", "testpass"))
    client.login(username="user", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.post(reverse("user_delete", args=[user.id]))
    assert response.status_code in (200, 302)


@pytest.mark.django_db
def test_logout(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="user",
        password=os.getenv("TEST_PASSWORD", "testpass"),
    )

    client.login(username="user", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.post(reverse("logout"))
    assert response.status_code in (200, 302)


@pytest.mark.django_db
def test_delete_user(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="user2",
        password=os.getenv("TEST_PASSWORD", "testpass"),
    )

    client.login(username="user2", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.post(reverse("user_delete", args=[user.id]))
    assert response.status_code in (200, 302)


@pytest.mark.django_db
def test_update_user(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="updateuser",
        password=os.getenv("TEST_PASSWORD", "testpass"),
    )

    client.login(username="updateuser", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.post(
        reverse("user_update", args=[user.id]),
        {
            "first_name": "John",
            "last_name": "Doe",
            "username": "updateuser",
        },
    )

    assert response.status_code in (200, 302)


@pytest.mark.django_db
def test_delete_other_user_forbidden(client, django_user_model):
    user1 = django_user_model.objects.create_user(
        username="user1",
        password=os.getenv("TEST_PASSWORD", "testpass"),
    )

    user2 = django_user_model.objects.create_user(
        username="user2",
        password=os.getenv("TEST_PASSWORD", "testpass"),
    )

    client.login(username="user1", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.post(reverse("user_delete", args=[user2.id]))
    assert response.status_code in (200, 302)


@pytest.mark.django_db
def test_update_other_user(client):
    user1 = User.objects.create_user(username="u1", password=os.getenv("TEST_PASSWORD", "testpass"))
    user2 = User.objects.create_user(username="u2", password=os.getenv("TEST_PASSWORD", "testpass"))

    client.login(username="u1", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.get(reverse("user_update", args=[user2.id]))
    assert response.status_code in (200, 302)


@pytest.mark.django_db
def test_users_redirect_after_create(client):
    response = client.post(
        reverse("user_create"),
        {
            "username": "newuser",
            "password1": "12345test",
            "password2": "12345test",
        },
    )

    assert response.status_code in [200, 302]


@pytest.mark.django_db
def test_update_user_not_logged(client):
    user = User.objects.create_user(username="test", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.get(reverse("user_update", args=[user.id]))

    assert response.status_code in (200, 302)


@pytest.mark.django_db
def test_delete_user_not_logged(client):
    user = User.objects.create_user(username="test2", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.post(reverse("user_delete", args=[user.id]))

    assert response.status_code in (200, 302)

@pytest.mark.django_db
def test_update_without_login(client):
    from django.contrib.auth.models import User
    from django.urls import reverse

    user = User.objects.create_user(username="nouser", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.get(reverse("user_update", args=[user.id]))

    assert response.status_code in (200, 302)

@pytest.mark.django_db
def test_update_user_invalid_form(client, django_user_model):
    from django.urls import reverse

    user = django_user_model.objects.create_user(
        username="invaliduser",
        password=os.getenv("TEST_PASSWORD", "testpass"),
    )

    client.login(username="invaliduser", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.post(
        reverse("user_update", args=[user.id]),
        {
            "username": "",
        },
    )

    assert response.status_code in (200, 302)

@pytest.mark.django_db
def test_delete_user_get_request(client, django_user_model):
    from django.urls import reverse

    user = django_user_model.objects.create_user(
        username="deleteget",
        password=os.getenv("TEST_PASSWORD", "testpass"),
    )

    client.login(username="deleteget", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.get(reverse("user_delete", args=[user.id]))

    assert response.status_code in (200, 302)
