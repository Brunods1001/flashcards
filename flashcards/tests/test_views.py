from unittest.case import skip

from .base import FlashTestCase
from flashcards.models import Flashcard


class HomeView(FlashTestCase):

    def test_template(self):
        self.check_template('/', 'flashcards/home.html')

    def test_card_creation_works(self):
        dict_create_card = {
            'title': 'My card title',
            'front-text': 'What is the mass of the sun?',
            'back-text': '1.989*10^30 kg',
        }
        response = self.client.post(path='/create', data=dict_create_card)
        card = Flashcard.objects.first()

        self.assertEqual(dict_create_card['title'], card.title)


    def test_card_creation_redirects_home(self):
        dict_create_card = {
            'title': 'My card title',
            'front_text': 'What is the mass of the sun?',
            'back_text': '1.989*10^30 kg',
        }
        response = self.client.post(path='/create', data=dict_create_card)
        self.assertRedirects(response, '/')
