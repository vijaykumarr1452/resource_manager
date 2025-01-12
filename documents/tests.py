from django.test import TestCase
from django.contrib.auth.models import User
from .models import Document

class DocumentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        Document.objects.create(title='Test Doc', user=self.user)

    def test_document_creation(self):
        doc = Document.objects.get(title='Test Doc')
        self.assertEqual(doc.user.username, 'testuser')
