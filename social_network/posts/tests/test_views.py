from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Post

User = get_user_model()


class PostPagesTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='TestUser')
        Post.objects.create(
            text='Test text',
            author=cls.user
        )

    def setUp(self):
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_pages_used_correct_template(self):
        templates_pages_names = {
            'posts/index.html': reverse('posts:index'),
            'posts/group_list.html': reverse('posts:group_list'),
            'posts/profile.html': reverse('posts:profile'),
            'posts/post_detail.html': reverse('posts:post_detail'),
            'posts/create_post.html': reverse('posts:post_edit'),
            'posts/create_post.html': reverse('posts:create_post'),
        }
