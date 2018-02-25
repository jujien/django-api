from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.


class DemoTest(APITestCase):
    def demo_test(self):
        response = self.client.get('http://127.0.0.1:8000/users/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)