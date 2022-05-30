from django.test import TestCase
from django.shortcuts import reverse


# Create your tests here.
class NotesNotesListviewsTest(TestCase):
    def test_notes_list_views_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_notes_list_views_by_name(self):
        response = self.client.get(reverse('notes_list'))
