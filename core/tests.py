from django.test import TestCase

class HelloWorldTest(TestCase):
    def test_hello_world(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Olá Mundo")
