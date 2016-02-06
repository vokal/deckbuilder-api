from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

import base64


class TestUserMixin(object):

    def setUp(self):
        self.username = 'esquire'
        self.email = 'bill@billadnted.com'
        self.password = 'a1b2c3d4'
        self.first_name = 'Bill'
        self.last_name = 'Preston'

        user = get_user_model().objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name)
        assert(user)
        self.user = user
        self.auth = {'Authorization': 'Basic ' + str(base64.b64encode(b'esquire:a1b2c3d4'))}


class TestUserRegistration(APITestCase):
    def test_register_user(self):
        data = {
            'username': 'theodore',
            'email': 'ted@billandted.com',
            'password': 'z1y2x3w4',
            'first_name': 'Ted',
            'last_name': 'Logan'
        }

        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['id'])
