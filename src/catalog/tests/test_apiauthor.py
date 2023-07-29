from rest_framework.test import APITestCase
from django.urls import reverse
from catalog.models import Author
from catalog.serializers import AuthorSerializer
from rest_framework import status

class AuthorApiTestCase(APITestCase):

    def test_get(self):
        author_1=Author.objects.create(first_name = "The test first_name author 1", last_name = "The test last_name author 1")
        author_2=Author.objects.create(first_name = "The test first_name author 2", last_name = "The test last_name author 2")
        url = reverse('catalog:author-list')
        response=self.client.get(url)
        serializer_data = AuthorSerializer([author_1, author_2], many=True).data        
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)