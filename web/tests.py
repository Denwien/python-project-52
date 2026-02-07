from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserCRUDTest(TestCase):

    def test_create_user(self):
        response = self.client.post(reverse('user_create'), {
            'username': 'newuser',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_update_user(self):
        user = User.objects.create_user(username='test', password='Test12345!')
        self.client.login(username='test', password='Test12345!')

        response = self.client.post(
            reverse('user_update', args=[user.id]),
            {'username': 'updated'}
        )

        self.assertRedirects(response, reverse('users'))
        user.refresh_from_db()
        self.assertEqual(user.username, 'updated')

    def test_delete_user(self):
        user = User.objects.create_user(username='delete', password='Test12345!')
        self.client.login(username='delete', password='Test12345!')

        response = self.client.post(reverse('user_delete', args=[user.id]))
        self.assertRedirects(response, reverse('users'))
        self.assertFalse(User.objects.filter(username='delete').exists())
