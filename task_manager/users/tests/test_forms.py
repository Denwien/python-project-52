import os
import pytest
import pytest
from django.contrib.auth.models import User

from task_manager.users.forms import UserCreateForm, UserUpdateForm


@pytest.mark.django_db
def test_user_create_form_passwords_do_not_match():
    form = UserCreateForm(
        data={
            "username": "user1",
            "password1": "12345",
            "password2": "54321",
        }
    )
    assert not form.is_valid()
    assert "password2" in form.errors


@pytest.mark.django_db
def test_user_create_form_short_password():
    form = UserCreateForm(
        data={
            "username": "user2",
            "password1": "12",
            "password2": "12",
        }
    )
    assert not form.is_valid()
    assert "password2" in form.errors


@pytest.mark.django_db
def test_user_create_form_saves_hashed_password():
    form = UserCreateForm(
        data={
            "username": "user3",
            "password1": "12345",
            "password2": "12345",
        }
    )
    assert form.is_valid()
    user = form.save()
    assert user.check_password("12345")


@pytest.mark.django_db
def test_user_update_form_duplicate_username():
    User.objects.create_user(username="existing", password=os.getenv("TEST_PASSWORD", "testpass"))
    user = User.objects.create_user(username="user", password=os.getenv("TEST_PASSWORD", "testpass"))

    form = UserUpdateForm(
        instance=user,
        data={"username": "existing"},
    )

    assert not form.is_valid()
@pytest.mark.django_db
def test_user_create_duplicate_username(client):
    from django.urls import reverse
    from django.contrib.auth.models import User

    User.objects.create_user(username="user", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.post(
        reverse("user_create"),
        {
            "username": "user",
            "password1": "12345",
            "password2": "12345",
        },
    )

    assert response.status_code == 200

@pytest.mark.django_db
def test_user_creation_password_mismatch(client):
    from django.urls import reverse

    response = client.post(
        reverse("user_create"),
        {
            "username": "user123",
            "password1": "12345",
            "password2": "54321",
        },
    )

    assert response.status_code == 200

@pytest.mark.django_db
def test_user_creation_without_names(client):
    from django.urls import reverse

    response = client.post(
        reverse("user_create"),
        {
            "username": "user_new",
            "password1": "12345test",
            "password2": "12345test",
            "first_name": "",
            "last_name": "",
        },
    )

    assert response.status_code in [200, 302]

@pytest.mark.django_db
def test_user_create_duplicate_username(client):
    from django.urls import reverse
    from django.contrib.auth.models import User

    User.objects.create_user(username="duplicate", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.post(
        reverse("user_create"),
        {
            "username": "duplicate",
            "password1": "12345test",
            "password2": "12345test",
        },
    )

    assert response.status_code == 200

@pytest.mark.django_db
def test_user_create_duplicate_username(client):
    from django.contrib.auth.models import User
    from django.urls import reverse

    User.objects.create_user(username="duplicate", password=os.getenv("TEST_PASSWORD", "testpass"))

    response = client.post(
        reverse("user_create"),
        {
            "username": "duplicate",
            "password1": "12345test",
            "password2": "12345test",
        },
    )

    assert response.status_code == 200

@pytest.mark.django_db
def test_user_create_invalid_password(client):
    from django.urls import reverse

    response = client.post(
        reverse("user_create"),
        {
            "username": "userx",
            "password1": "123",
            "password2": "456",
        },
    )

    assert response.status_code == 200

@pytest.mark.django_db
def test_user_create_password_mismatch(client):
    from django.urls import reverse

    response = client.post(
        reverse("user_create"),
        {
            "username": "user_mismatch",
            "password1": "password123",
            "password2": "different123",
        },
    )

    assert response.status_code == 200
