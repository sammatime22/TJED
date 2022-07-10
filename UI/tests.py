import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import DailySearchMetadata
from .views import KanjiResultsPageView
from API.tests import create_kanji, create_vocab
from unittest.mock import patch

# Factory methods to assist the UI tests.
def create_search_metrics(date, number_of_searches):
    DailySearchMetadata.objects.create(date=date, number_of_searches=number_of_searches)

# Create your tests here.
class KanjiResultsPageViewTests(TestCase):
    '''
    Tests used to ensure the appropriate data is displayed on the 
    Results page (for Kanji).
    '''
    # The status code is 200 and information about the Kanji is returned
    def test_kanji_search_comes_back_with_kanji_results(self):
        create_kanji(kanji_character='日', meaning="day, Sun", on_yomi="ニチ、ジツ", kun_yomi="ひ、ーぴ、ーか")
        response = self.client.get(reverse('ui:kanji', args=('日',)))
        assert response.status_code == 200
        decoded_content = response.content.decode('utf-8')
        assert decoded_content.find("<li>Kanji: 日</li>") > -1
        assert decoded_content.find("<li>On-Yomi: ニチ、ジツ</li>") > -1
        assert decoded_content.find("<li>Kun-Yomi: ひ、ーぴ、ーか </li>") > -1
        assert decoded_content.find("<li>Meaning: day, Sun </li>") > -1
        assert decoded_content.find("<h3>Today's Search Metrics</h3>") > -1
        assert decoded_content.find("<h2>Number of Searches: 1</h2>") > -1


    # The status code is 404 and no Kanji info is returned, described in the message
    def test_kanji_search_comes_back_without_results(self):
        response = self.client.get(reverse('ui:kanji', args=('日',)))
        assert response.status_code == 404
        decoded_content = response.content.decode('utf-8')
        assert decoded_content.find("<h5>No Kanji could be found via this search.</h5>") > -1
        assert decoded_content.find("<h3>Today's Search Metrics</h3>") > -1
        assert decoded_content.find("<h2>Number of Searches: 1</h2>") > -1


    # The status code is 400, and no Kanji info is returned, described in the message
    def test_kanji_search_is_a_bad_request(self):
        response = self.client.get(reverse('ui:kanji', args=('日曜日',)))
        assert response.status_code == 400
        decoded_content = response.content.decode('utf-8')
        assert decoded_content.find("<h5>The query parameters provided were not of an appropriate length.</h5>") > -1
        assert decoded_content.find("<h3>Today's Search Metrics</h3>") > -1
        assert decoded_content.find("<h2>Number of Searches: 1</h2>") > -1


    # The status code is 500, and explicitly states an Internal Server Error occurred
    @patch('UI.models.DailySearchMetadata.objects.filter')
    def test_kanji_search_causes_internal_server_error(self, mock_corrupt_filter):
        mock_corrupt_filter.side_effect = Exception
        response = self.client.get(reverse('ui:kanji', args=('日',)))
        assert response.status_code == 500
        decoded_content = response.content.decode('utf-8')
        assert decoded_content.find("<p>Internal Server Error</p>") > -1


class VocabResultsPageViewTests(TestCase):
    '''
    Tests used to test the resolving of Vocab data on the Results page.
    '''
    # 200 w/kanji search
    def test_japanese_vocab_search_comes_back_with_vocab_results(self):
        vocab_of_interest = create_vocab(japanese_word="日", kana="にち", english_word="Sun")
        response = self.client.get(reverse('ui:vocab_from_japanese', args=("日",)))
        assert response.status_code == 200
        decoded_content = response.content.decode('utf-8')
        assert decoded_content.find("<li>Japanese Word: 日</li>") > -1
        assert decoded_content.find("<li>Kana (reading): にち </li>") > -1
        assert decoded_content.find("<li>English Word: Sun</li>") > -1
        assert decoded_content.find("<h3>Today's Search Metrics</h3>") > -1
        assert decoded_content.find("<h2>Number of Searches: 1</h2>") > -1


    # Kana search 200
    def test_japanese_vocab_search_using_kana_comes_back_with_vocab_results(self):
        vocab_of_interest = create_vocab(japanese_word="日", kana="にち", english_word="Sun")
        response = self.client.get(reverse('ui:vocab_from_japanese', args=("にち",)))
        assert response.status_code == 200
        decoded_content = response.content.decode('utf-8')
        assert decoded_content.find("<li>Japanese Word: 日</li>") > -1
        assert decoded_content.find("<li>Kana (reading): にち </li>") > -1
        assert decoded_content.find("<li>English Word: Sun</li>") > -1
        assert decoded_content.find("<h3>Today's Search Metrics</h3>") > -1
        assert decoded_content.find("<h2>Number of Searches: 1</h2>") > -1


    # Test that a we try the Japanese search but do not get anything back and status code 404
    def test_japanese_vocab_search_comes_back_without_vocab_results(self):
        response = self.client.get(reverse('ui:vocab_from_japanese', args=("日",)))
        assert response.status_code == 404
        decoded_content = response.content.decode('utf-8')
        assert decoded_content.find("<h5>No Vocab could be found via the Japanese term provided.</h5>") > -1
        assert decoded_content.find("<h3>Today's Search Metrics</h3>") > -1
        assert decoded_content.find("<h2>Number of Searches: 1</h2>") > -1


    # Test Japanese Vocab 500
    @patch('API.models.Vocab.objects.filter')
    def test_japanese_vocab_search_has_internal_server_error(self, mock_corrupt_filter):
        mock_corrupt_filter.side_effect = Exception
        response = self.client.get(reverse('ui:vocab_from_japanese', args=("日",)))
        assert response.status_code == 500
        decoded_content = response.content.decode('utf-8')
        assert decoded_content.find("<p>Internal Server Error</p>") > -1


    # Test that a proper English search returns vocab results and status code 200
    def test_english_vocab_search_comes_back_with_vocab_results(self):
        create_vocab(japanese_word="日", kana="にち", english_word="Sun")
        response = self.client.get(reverse('ui:vocab_from_english', args=("Sun",)))
        assert response.status_code == 200
        decoded_content = response.content.decode('utf-8')
        assert decoded_content.find("<li>Japanese Word: 日</li>") > -1
        assert decoded_content.find("<li>Kana (reading): にち </li>") > -1
        assert decoded_content.find("<li>English Word: Sun</li>") > -1
        assert decoded_content.find("<h3>Today's Search Metrics</h3>") > -1
        assert decoded_content.find("<h2>Number of Searches: 1</h2>") > -1
    

    # Test that a we try the English search but do not get anything back and status code 404
    def test_english_vocab_search_comes_back_without_vocab_results(self):
        response = self.client.get(reverse('ui:vocab_from_english', args=("Sun",)))
        assert response.status_code == 404
        decoded_content = response.content.decode('utf-8')
        assert decoded_content.find("<h5>No Vocab could be found via the English term provided.</h5>") > -1
        assert decoded_content.find("<h3>Today's Search Metrics</h3>") > -1
        assert decoded_content.find("<h2>Number of Searches: 1</h2>") > -1


    # Test English Vocab 500
    @patch('API.models.Vocab.objects.filter')
    def test_english_vocab_search_has_internal_server_error(self, mock_corrupt_filter):
        mock_corrupt_filter.side_effect = Exception
        response = self.client.get(reverse('ui:vocab_from_english', args=("Sun",)))
        assert response.status_code == 500
        decoded_content = response.content.decode('utf-8')
        assert decoded_content.find("<p>Internal Server Error</p>") > -1


    # Test Overarching View 500
    @patch('UI.models.DailySearchMetadata.objects.filter')
    def test_vocab_search_has_internal_server_error(self, mock_corrupt_filter):
        mock_corrupt_filter.side_effect = Exception
        response = self.client.get(reverse('ui:vocab_from_english', args=("Sun",)))
        assert response.status_code == 500
        decoded_content = response.content.decode('utf-8')
        assert decoded_content.find("<p>Internal Server Error</p>") > -1
