from django.test import TestCase
from django.shortcuts import reverse
from .models import Notes


# Create your tests here.
class NotesNotesListviewsTest(TestCase):
    def setUp(self):
        self.note_obj =Notes.objects.create(author="khodam", text="sample text.")
    def test_notes_list_views_url(self):
        response = self.client.get('/') #boro be browser  va ba client (masalan karbar dare darkhast mide)va get request befrest va javab ro bargardoon
        self.assertEqual(response.status_code, 200)  # barresi mikone ke jaavb barabar ba 200 hast ya na  ! 200 yani dardastres hastesh ya na

    def test_notes_list_views_by_name(self):
        response = self.client.get(reverse('notes_list'))
        # yani esme url ro migire va kar ro barax anjam mide
        # mire bebine  url name ghare che methodi ro ejra kone va masir ro barax mire

    def test_notes_list_page(self):
        response = self.client.get(reverse("notes_list"))
        self.assertContains(response,self.note_obj.text)

