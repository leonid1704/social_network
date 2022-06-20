from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()


class UsersURLTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user')
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_urls_guest_client_response_code(self):
        urls_response_codes = {
            '/auth/signup/': 200,
            '/auth/login/': 200,
            '/auth/password_change/': 302,
            '/auth/password_reset/': 200,
            '/auth/logout/': 200,
        }
        for url, response_code in urls_response_codes.items():
            with self.subTest(url=url):
                response = self.guest_client.get(url).status_code
                self.assertEqual(response, response_code)

    def test_urls_authorized_client_response_code(self):
        urls_response_codes = {
            '/auth/signup/': 200,
            '/auth/login/': 200,
            '/auth/password_change/': 200,
            '/auth/password_reset/': 200,
            '/auth/logout/': 200,
        }
        for url, response_code in urls_response_codes.items():
            with self.subTest(url=url):
                response = self.authorized_client.get(url).status_code
                self.assertEqual(response, response_code)

    def test_urls_templates_used(self):
        urls_templates_used = {
            '/auth/signup/': 'users/signup.html',
            '/auth/login/': 'users/login.html',
            '/auth/password_change/': 'users/password_change.html',
            '/auth/password_reset/': 'users/password_reset.html',
            '/auth/logout/': 'users/logged_out.html',
        }

        for url, template_used in urls_templates_used.items():
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertTemplateUsed(response, template_used)
