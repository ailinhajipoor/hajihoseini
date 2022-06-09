from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your tests here.
class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="ailin")
        cls.post = Post.objects.create(
            title="Post1",
            text="this is the description of post 1",
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user,
        )
        cls.post2 = Post.objects.create(
            title="Post2",
            text="A draft post",
            status=Post.STATUS_CHOICES[1][0],
            author=cls.user,
        )

    # def setUp(self):


    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_page(self):
        response = self.client.get(reverse('posts_list'))
        # self.assertContains(response,"Post1")
        self.assertContains(response, self.post.title)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view_by_name(self):
        response = self.client.get(reverse('posts_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_blog_detail_page(self):
        response = self.client.get(f'/blog/{self.post.id}/')
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.text)

    def test_post_details_on_blog_detail_page_by_name(self):
        response = self.client.get(reverse('posts_detail', args=[self.post.id]))
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.text)

    def test_status_404_if_post_id_exist(self):
        response = self.client.get(reverse('posts_detail', args=[200]))
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_in_posts_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post.title)
        self.assertNotContains(response, self.post2.title)
