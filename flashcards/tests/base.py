from django.test import TestCase


class FlashTestCase(TestCase):

    def check_template(self, url, template):
        response = self.client.get(url)
        self.assertTemplateUsed(response, template)
