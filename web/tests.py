from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Status


class StatusCRUDTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test", password="Test12345!")
        self.client.login(username="test", password="Test12345!")

    def test_create_status(self):
        response = self.client.post(
            reverse("status_create"),
            {
                "name": "New",
            },
        )
        self.assertRedirects(response, reverse("statuses"))
        self.assertTrue(Status.objects.filter(name="New").exists())

    def test_update_status(self):
        status = Status.objects.create(name="Old")
        response = self.client.post(
            reverse("status_update", args=[status.id]), {"name": "Updated"}
        )
        self.assertRedirects(response, reverse("statuses"))
        status.refresh_from_db()
        self.assertEqual(status.name, "Updated")

    def test_delete_status(self):
        status = Status.objects.create(name="To delete")
        response = self.client.post(reverse("status_delete", args=[status.id]))
        self.assertRedirects(response, reverse("statuses"))
        self.assertFalse(Status.objects.filter(id=status.id).exists())
