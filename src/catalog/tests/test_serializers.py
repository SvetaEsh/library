from django.test import TestCase
from catalog.models import Author
from catalog.serializers import AuthorSerializer

class AuthorSerializerTestCase(TestCase):
    def test_ok(self):
        author_1=Author.objects.create(first_name = "The test first_name author 1", last_name = "The test last_name author 1")
        author_2=Author.objects.create(first_name = "The test first_name author 2", last_name = "The test last_name author 2")
        data = AuthorSerializer([author_1, author_2], many=True).data
        expected_data=[
            {
                "id": author_1.id,
                "first_name" : "The test first_name author 1",
                "last_name" : "The test last_name author 1",
                "date_of_birth" : None,
                "date_of_death" : None
            },
            {
                "id": author_2.id,
                "first_name" : "The test first_name author 2",
                "last_name" : "The test last_name author 2",
                "date_of_birth" : None,
                "date_of_death" : None
            }
        ]
        self.assertEqual(expected_data, data)