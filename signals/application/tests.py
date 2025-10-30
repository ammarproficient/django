from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse

class PostTestCase(TestCase):
    def setUp(self):
        # test user create karo
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()

        # ek post create karo
        self.post = Post.objects.create(
            user=self.user,
            title='Test Post',
            content='Test content'
        )

    def test_create_post_requires_login(self):
        # login nahi hone par create page redirect kare
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 302)  # redirect to login

        # login karke create post
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('create_post'), {
            'title': 'New Post',
            'content': 'Some content'
        })
        self.assertEqual(response.status_code, 302)  # redirect home
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_delete_post_requires_login(self):
        # login nahi hone par delete redirect kare
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)  # redirect to login

        # login karke delete post
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())
