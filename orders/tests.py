from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class MyOrderViewTests(TestCase):
    def test_no_logged_user_should_redirect(self):
        url = reverse("my_order")
        response = self.client.get(url)
        self.assertRedirects(response, "/users/login/?next=/orders/my-order")

    def test_logged_user_should_redirect(self):
        url = reverse("my_order")
        user = get_user_model().objects.create(username="test")
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
