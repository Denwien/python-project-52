from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Label, Status, Task


class StatusCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="Test12345!",
        )
        self.client.login(
            username="test",
            password="Test12345!",
        )

    def test_create_status(self):
        response = self.client.post(
            reverse("status_create"),
            {
                "name": "New",
            },
        )
        self.assertRedirects(
            response,
            reverse("statuses"),
        )
        self.assertTrue(
            Status.objects.filter(name="New").exists(),
        )

    def test_update_status(self):
        status = Status.objects.create(name="Old")
        response = self.client.post(
            reverse("status_update", args=[status.id]),
            {
                "name": "Updated",
            },
        )
        self.assertRedirects(
            response,
            reverse("statuses"),
        )
        status.refresh_from_db()
        self.assertEqual(status.name, "Updated")

    def test_delete_status(self):
        status = Status.objects.create(name="Delete")
        response = self.client.post(
            reverse("status_delete", args=[status.id]),
        )
        self.assertRedirects(
            response,
            reverse("statuses"),
        )
        self.assertFalse(
            Status.objects.filter(id=status.id).exists(),
        )


class TaskCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="author",
            password="Test12345!",
        )
        self.status = Status.objects.create(
            name="New",
        )
        self.client.login(
            username="author",
            password="Test12345!",
        )

    def test_create_task(self):
        response = self.client.post(
            reverse("task_create"),
            {
                "name": "Task 1",
                "description": "Desc",
                "status": self.status.id,
            },
        )
        self.assertRedirects(
            response,
            reverse("tasks"),
        )
        self.assertTrue(
            Task.objects.filter(name="Task 1").exists(),
        )

    def test_update_task(self):
        task = Task.objects.create(
            name="Old",
            status=self.status,
            author=self.user,
        )
        response = self.client.post(
            reverse("task_update", args=[task.id]),
            {
                "name": "Updated",
                "status": self.status.id,
            },
        )
        self.assertRedirects(
            response,
            reverse("tasks"),
        )

    def test_delete_task(self):
        task = Task.objects.create(
            name="Delete",
            status=self.status,
            author=self.user,
        )
        response = self.client.post(
            reverse("task_delete", args=[task.id]),
        )
        self.assertRedirects(
            response,
            reverse("tasks"),
        )
        self.assertFalse(
            Task.objects.filter(id=task.id).exists(),
        )


class LabelCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="label",
            password="Test12345!",
        )
        self.client.login(
            username="label",
            password="Test12345!",
        )

    def test_create_label(self):
        response = self.client.post(
            reverse("label_create"),
            {"name": "Bug"},
        )
        self.assertRedirects(
            response,
            reverse("labels"),
        )
        self.assertTrue(
            Label.objects.filter(name="Bug").exists(),
        )

    def test_update_label(self):
        label = Label.objects.create(name="Old")
        response = self.client.post(
            reverse("label_update", args=[label.id]),
            {"name": "New"},
        )
        self.assertRedirects(
            response,
            reverse("labels"),
        )

    def test_delete_label(self):
        label = Label.objects.create(name="Temp")
        response = self.client.post(
            reverse("label_delete", args=[label.id]),
        )
        self.assertRedirects(
            response,
            reverse("labels"),
        )
        self.assertFalse(
            Label.objects.filter(id=label.id).exists(),
        )


class TaskFilterTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="filteruser",
            password="Test12345!",
        )
        self.other = User.objects.create_user(
            username="other",
            password="Test12345!",
        )
        self.status = Status.objects.create(name="new")
        self.label = Label.objects.create(name="bug")

        self.task1 = Task.objects.create(
            name="My task",
            status=self.status,
            author=self.user,
        )
        self.task1.labels.add(self.label)

        self.task2 = Task.objects.create(
            name="Other task",
            status=self.status,
            author=self.other,
        )

        self.client.login(
            username="filteruser",
            password="Test12345!",
        )

    def test_filter_only_self_tasks(self):
        response = self.client.get(
            reverse("tasks"),
            {"self_tasks": "on"},
        )
        self.assertContains(response, "My task")
        self.assertNotContains(response, "Other task")

    def test_filter_by_label(self):
        response = self.client.get(
            reverse("tasks"),
            {"labels": self.label.id},
        )
        self.assertContains(response, "My task")
        self.assertNotContains(response, "Other task")
