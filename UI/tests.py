import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import DailySearchMetadata
from API.models import Kanji, Vocab
from API.tests import create_kanji
from API.tests import create_vocab

# Factory methods to assist the UI tests.
def create_search_metrics(date, number_of_searches):
    DailySearchMetadata.objects.create(date=date, number_of_searches=number_of_searches)

# Create your tests here.
class KanjiResultsPageViewTests(TestCase):
    '''
    Tests used to ensure the appropriate data is displayed on the 
    Results page (for Kanji).
    '''
    def test_kanji_search_comes_back_with_kanji_results(self):
        kanji_of_interest = create_kanji(kanji_character='日', meaning="day, Sun", on_yomi="ニチ、ジツ", kun_yomi="ひ、ーぴ、ーか")
        url = reverse('ui:kanji', args=(kanji_of_interest.kanji_character,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # also assert that the expected "kanji" data was returned

    def test_kanji_search_comes_back_without_results(self):
        url = revers('ui:kanji', args=("just_something_random",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        # Ensure the empty page still has attributes we would expect


class VocabResultsPageViewTests(TestCase):
    '''
    Tests used to test the resolving of Vocab data on the Results page.
    '''
    def test_english_vocab_search_comes_back_with_vocab_results(self):
        vocab_of_interest = create_vocab(japanese_word="日", kana="にち", english_word="Sun")
        url = reverse('ui:eng', args=(vocab_of_interest.english_word,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # also assert that the expected "vocab" data was returned

    def test_japanese_vocab_search_comes_back_with_vocab_results(self):
        vocab_of_interest = create_vocab(japanese_word="日", kana="にち", english_word="Sun")
        url = reverse('ui:jpn', args=(vocab_of_interest.japanese_word,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # again, assert that the expected "vocab" data was returned

    def test_search_comes_back_without_results(self):
        url = reverse('ui:eng', args=("wazaaap",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        # Ensure the empty page still has attributes we would expect
