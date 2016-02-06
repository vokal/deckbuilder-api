from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from user.tests import TestUserMixin


class CardTests(TestUserMixin, APITestCase):

    def test_get_card_list(self):
        url = reverse('card-list')
        response = self.client.get(url, **self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_get_card_detail(self):
        url = reverse('card-list')
        response = self.client.get(url, **self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        pk = response.data['results'][0]['id']

        url = reverse('card-detail', kwargs={'pk': pk})
        response = self.client.get(url, **self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('text', response.data)
        self.assertIn('rarity', response.data)
