import json
from django.test import TestCase
from apps.subscribe.models import Subscriptor


class SubscriptorTestCase(TestCase):

    def setUp(self):
        Subscriptor.objects.create(
            client="12345",
            account="12345",
            coupon_used="12345",
        )

    def test_valid_clients(self):
        subscriber = Subscriptor.objects.get(client="12345")
        self.assertEqual(subscriber.client, "12345")

    def test_wrong_subscribe_view(self):
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
        users = [
            {
                "client": 20476348,
                "account": 602364702,
            },
            {
                "client": 170110576,
                "account": 667861859,
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
                "client": 20476666,
                "account": 602364702,
            },
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
            self.assertEqual(dresponse.get("code"), 500)
