from django.test import TestCase

from .base import FlashTestCase
from flashcards.models import Flashcard


class FlashcardModel(FlashTestCase):

    def test_saving_items(self):
        first = Flashcard(title='title', front_text='front', back_text='back')
        first.save()

        second = Flashcard(title='title2', front_text='front2',
                           back_text='back2')
        second.save()

        self.assertEqual(Flashcard.objects.all().count(), 2)

    def test_saving_items(self):
        first = Flashcard(title='title', front_text='front', back_text='back')
        first.save()

        second = Flashcard(title='title2', front_text='front2',
                           back_text='back2')
        second.save()

        self.assertEqual(first.title, 'title')
        self.assertEqual(second.title, 'title2')

