import json
from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.subscribe.models import Subscriptor


class SubscriptorTestCase(TestCase):

    def setUp(self):
        Subscriptor.objects.create(
            client="12345",
            account="12345",
        )
        User = get_user_model()
        User.objects.create_user(
            email="oscar0@flikn.com",
            password="123456",
        )
        User.objects.create_user(
            email="oscar1@flikn.com",
            password="123456",
        )
        User.objects.create_user(
            email="oscar2@flikn.com",
            password="123456",
        )
        User.objects.create_user(
            email="oscar3@flikn.com",
            password="123456",
        )

    def test_valid_clients(self):
        subscriber = Subscriptor.objects.get(client="12345")
        self.assertEqual(subscriber.client, 12345)

    def test_wrong_subscribe_view(self):
        self.client.login(
            email="oscar0@flikn.com",
            password="123456",
        )

        users = [
            {
                "client": "20476348a",
                "account": "602364702",
            },
            {
                "client": "170110576",
                "account": "b667861859",
            },
        ]
        for user in users:
            response = self.client.post('/api/subscribe/', data=user)
            self.assertEqual(response.status_code, 200)
            dresponse = json.loads(response.content)
            # Check that the json response code is invalid. Payload is
            # syntactically incorrect Payload.
            self.assertEqual(dresponse.get("code"), 400)

    def test_successful_subscribe_view(self):
        self.client.login(
            email="oscar0@flikn.com",
            password="123456",
        )

        users = [
            {
                "client": 20476348,
                "account": 602364702,
            },
        ]
        for user in users:
            response = self.client.post('/api/subscribe/', data=user)
            self.assertEqual(response.status_code, 200)
            dresponse = json.loads(response.content)
            # Check that the json response code is successful.
            self.assertEqual(dresponse.get("code"), 200)

        users = [
            {
                "client": 170110666,
                "account": 667861859,
            },
        ]
        for user in users:
            response = self.client.post('/api/subscribe/', data=user)
            self.assertEqual(response.status_code, 200)
            dresponse = json.loads(response.content)
            # Check that the json response code is invalid. Client is not
            # valid.
            self.assertEqual(dresponse.get("code"), 403)

    def test_unique_successful_subscribe_view(self):
        self.client.login(
            email="oscar0@flikn.com",
            password="123456",
        )

        unique_users = [
            {
                "client": 20476348,
                "account": 602364702,
            },
            {
                "client": 170110576,
                "account": 667861859,
            },
        ]

        # Get method shouldn't change anything.
        for unique_user in unique_users:
            response = self.client.get('/api/subscribe/', data=unique_user)
            self.assertEqual(response.status_code, 200)
            dresponse = json.loads(response.content)
            self.assertEqual(dresponse.get("code"), 200)

            response = self.client.get('/api/subscribe/', data=unique_user)
            self.assertEqual(response.status_code, 200)
            dresponse = json.loads(response.content)
            self.assertEqual(dresponse.get("code"), 200)

        self.client.logout()

        unique_user = unique_users[0]
        for i in range(2, -1, -1):
            self.client.login(
                email="oscar%s@flikn.com" % i,
                password="123456",
            )
            # One client just can subscribe once.
            response = self.client.post(
                '/api/subscribe/',
                data=unique_user,
            )
            self.assertEqual(response.status_code, 200)
            dresponse = json.loads(response.content)
            # Check that the json response code is successful.
            self.assertEqual(dresponse.get("code"), 200)
            self.assertEqual(dresponse.get("lifetime"), i)
            self.client.logout()

        self.client.login(
            email="oscar3@flikn.com",
            password="123456",
        )
        # Client and account must not be on the DB.
        response = self.client.post('/api/subscribe/', data=unique_user)
        self.assertEqual(response.status_code, 200)
        dresponse = json.loads(response.content)
        # The response code must be restricted 403.
        self.assertEqual(dresponse.get("code"), 403)

        self.client.logout()

        unique_user = unique_users[1]
        for i in range(3):
            self.client.login(
                email="oscar%s@flikn.com" % i,
                password="123456",
            )
            # One client just can subscribe once.
            response = self.client.post(
                '/api/subscribe/',
                data=unique_user,
            )
            self.assertEqual(response.status_code, 200)
            dresponse = json.loads(response.content)
            # Check that the json response code is 403.
            self.assertEqual(dresponse.get("code"), 403)
            # self.assertEqual(dresponse.get("lifetime"), 3)
            self.client.logout()
