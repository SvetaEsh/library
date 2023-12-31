from django.test import TestCase
from catalog.models import Author

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Svetlana', last_name='Sasha')

    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_first_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)
    
    def test_get_absolute_url(self):
        author=Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(),'/catalog/author/1')
