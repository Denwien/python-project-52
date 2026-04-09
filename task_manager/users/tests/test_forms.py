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
    User.objects.create_user(username="existing", password="12345")
    user = User.objects.create_user(username="user", password="12345")

    form = UserUpdateForm(
        instance=user,
        data={"username": "existing"},
    )

    assert not form.is_valid()
@pytest.mark.django_db
def test_user_create_duplicate_username(client):
    from django.urls import reverse
    from django.contrib.auth.models import User

    User.objects.create_user(username="user", password="123")

    response = client.post(
        reverse("user_create"),
        {
            "username": "user",
            "password1": "12345",
            "password2": "12345",
        },
    )

    assert response.status_code == 200
