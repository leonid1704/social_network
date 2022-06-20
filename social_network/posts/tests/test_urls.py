from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from ..models import Post, Group

User = get_user_model()


class PostURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='no-name')
        cls.group = Group.objects.create(
            title='Test group',
            slug='test-slug',
            description='Test description',
        )
        cls.author = User.objects.create_user(username='author')
        cls.post = Post.objects.create(
            author=cls.author,
            text='Test post',
        )

    def setUp(self):
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.author_client = Client()
        self.author_client.force_login(self.author)

    def test_urls_guest_client_response_code(self):
        urls_response_codes = {
            '/': 200,
            '/create/': 302,
            '/group/test-slug/': 200,
            '/profile/no-name/': 200,
            f'/posts/{self.post.id}/': 200,
            f'/posts/{self.post.id}/edit/': 302,
            '/unexisting_page/': 404,
        }
        for url, response_code in urls_response_codes.items():
            with self.subTest(url=url):
                response = self.guest_client.get(url).status_code
                self.assertEqual(response, response_code)

    def test_urls_authorized_client_response_code(self):
        urls_response_codes = {
            '/': 200,
            '/create/': 200,
            '/group/test-slug/': 200,
            '/profile/no-name/': 200,
            f'/posts/{self.post.id}/': 200,
            f'/posts/{self.post.id}/edit/': 302,
            '/unexisting_page/': 404,
        }
        for url, response_code in urls_response_codes.items():
            with self.subTest(url=url):
                response = self.authorized_client.get(url).status_code
                self.assertEqual(response, response_code)

    def test_urls_author_client_response_code(self):
        urls_response_codes = {
            f'/posts/{self.post.id}/edit/': 200
        }
        for url, response_code in urls_response_codes.items():
            with self.subTest(url=url):
                response = self.author_client.get(url).status_code
                self.assertEqual(response, response_code)

    def test_urls_templates_used(self):
        urls_templates_used = {
            '/': 'posts/index.html',
            '/create/': 'posts/create_post.html',
            '/group/test-slug/': 'posts/group_posts.html',
            '/profile/no-name/': 'posts/profile.html',
            f'/posts/{self.post.id}/': 'posts/post_detail.html',
            f'/posts/{self.post.id}/edit/': 'posts/create_post.html',
        }
        for url, template_used in urls_templates_used.items():
            with self.subTest(url=url):
                response = self.author_client.get(url)
                self.assertTemplateUsed(response, template_used)
