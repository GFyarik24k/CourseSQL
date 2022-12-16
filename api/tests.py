from django.test import TestCase


from django.test import TestCase
from django.urls import reverse
import json
from rest_framework.test import APITestCase

class StudentTests(APITestCase):
    def test_get_correct(self):
        url = reverse('Getter', args=["20И573", "Ярослав", "Мажей", 'Владимирович'])
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content), [{
            "id": 1,
            "num": "20И573",
            "name": "Ярослав",
            "surname": "Мажей",
            "patronymic": "Владимирович"
        }])