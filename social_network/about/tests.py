from django.test import TestCase, Client


class AboutURLTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_urls_response(self):
        urls = ['/about/author/', '/about/tech/']
        status_code = 200
        for url in urls:
            with self.subTest(url=url):
                response = self.client.get(url).status_code
                self.assertEqual(response, status_code)
