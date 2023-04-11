import json

from django.test import TestCase
from rest_framework.test import APIClient


class TestResumeAPI(TestCase):
    TEST_RESUME = 1
    TEST_ENDPOINT = f'/resume/{TEST_RESUME}/'
    TEST_PATCH_DATA = {"status": "test_status"}

    fixtures = ['test_data.json']
    client = APIClient()

    def test_get(self):
        response = self.client.get(self.TEST_ENDPOINT)
        self.assertEqual(response.status_code, 200)

    def test_patch(self):
        response = self.client.patch(self.TEST_ENDPOINT, json.dumps(self.TEST_PATCH_DATA),
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(self.TEST_ENDPOINT)
        self.assertEqual(response.data[0]['status'], self.TEST_PATCH_DATA['status'])

