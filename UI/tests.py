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


    # The status code is 404 and no Kanji info is returned, described in the message
    def test_kanji_search_comes_back_without_results(self):
        response = self.client.get(reverse('ui:kanji', args=('日',)))
        assert response.status_code == 404
        assert response.content.decode('utf-8').find("<h5>No Kanji could be found via this search.</h5>") > -1


    # The status code is 400, and no Kanji info is returned, described in the message
    def test_kanji_search_is_a_bad_request(self):
        response = self.client.get(reverse('ui:kanji', args=('日曜日',)))
        assert response.status_code == 400
        assert response.content.decode('utf-8').find("<h5>The query parameters provided were not of an appropriate length.</h5>")


    # The status code is 500, and explicitly states an Internal Server Error occurred
    @patch('UI.models.DailySearchMetadata.objects.filter')
    def test_kanji_search_causes_internal_server_error(self, mock_corrupt_filter):
        mock_corrupt_filter.side_effect = Exception
        response = self.client.get(reverse('ui:kanji', args=('日',)))
        assert response.status_code == 500
        assert response.content.decode('utf-8').find("<p>Internal Server Error</p>") > -1


# class VocabResultsPageViewTests(TestCase):
#     '''
#     Tests used to test the resolving of Vocab data on the Results page.
#     '''
#     def test_english_vocab_search_comes_back_with_vocab_results(self):
#         vocab_of_interest = create_vocab(japanese_word="日", kana="にち", english_word="Sun")
#         url = reverse('ui:eng', args=(vocab_of_interest.english_word,))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         # also assert that the expected "vocab" data was returned

#     def test_japanese_vocab_search_comes_back_with_vocab_results(self):
#         vocab_of_interest = create_vocab(japanese_word="日", kana="にち", english_word="Sun")
#         url = reverse('ui:jpn', args=(vocab_of_interest.japanese_word,))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         # again, assert that the expected "vocab" data was returned

#     def test_search_comes_back_without_results(self):
#         url = reverse('ui:eng', args=("wazaaap",))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 404)
#         # Ensure the empty page still has attributes we would expect
