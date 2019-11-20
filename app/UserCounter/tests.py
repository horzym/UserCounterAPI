from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

import time


class PublicUserCounterApiTest(TestCase):
    """Test Publicly UserCounter API"""

    def setUp(self):
        self.client = APIClient()

    def testCountForCorrectUrl(self):
        user_id = 123
        url = reverse('user-counter', args=[user_id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def testCountForBadUserId(self):
        user_id = 9999999
        url = reverse('user-counter', args=[user_id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def testCountTooManyRequest(self):
        user_id = 122
        url = reverse('user-counter', args=[user_id])
        for i in range(1, 10):
            res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def testCheckCorrectContent(self):
        user_id = 122
        url = reverse('user-counter', args=[user_id])
        for i in range(0, 5):
            res = self.client.get(url)
            time.sleep(1)
        self.assertEqual(res.data['counter'], 5)
        payload = {
            "user_id": 122,
            "counter": 5
        }
        self.assertEqual(res.data, payload)

    def testForCorrectUserId(self):
        user_id = 122
        url = reverse('user-counter', args=[user_id])
        for i in range(0, 10):
            res = self.client.get(url)
            time.sleep(1)
        self.assertEqual(res.data['user_id'], user_id)

    def testForUnCorrectURL(self):
        url = 'localhost:8000/api/user/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
