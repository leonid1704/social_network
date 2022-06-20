from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='no-name')
        cls.post = Post.objects.create(
            author=cls.user,
            text='Test post',
        )

    def test_post_has_correct_object_names(self):
        self.assertEqual(self.post.text, str(self.post))

    def test_post_help_texts(self):
        post = self.post
        fields_help_texts = {
            'text': 'Enter post text',
            'group': 'Post will be added to this group',
        }
        for field, expected_value in fields_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).help_text, expected_value)


class GroupModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = Group.objects.create(
            title='Test group',
            slug='test-slug',
            description='Test description',
        )

    def test_group_have_correct_object_names(self):
        self.assertEqual(self.group.title, str(self.group))

    def test_group_help_texts(self):
        group = self.group
        fields_help_texts = {
            'title': 'Enter group title',
            'slug': 'Enter group slug',
            'description': 'Enter group description',
        }
        for field, expected_value in fields_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    group._meta.get_field(field).help_text, expected_value)
