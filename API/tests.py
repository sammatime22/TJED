from django.test import TestCase
from django.urls import reverse

from .models import Kanji, Vocab
from .views import get_kanji, get_vocab_using_japanese, get_vocab_using_english

import json
import unittest
from unittest.mock import patch

# Factory methods to facilitate testing
def create_kanji(kanji_character, meaning, on_yomi, kun_yomi):
    Kanji.objects.create(kanji_character=kanji_character, meaning=meaning, on_yomi=on_yomi, kun_yomi=kun_yomi)

def create_vocab(japanese_word, furigana, english_word):
    Vocab.objects.create(japanese_word=japanese_word, furigana=furigana, english_word=english_word)


# Create your tests here.
class KanjiViewTests(TestCase):
    # Test 200 response and content returned with available Kanji
    def test_kanji_search_returns_200(self):
        create_kanji(kanji_character='日', meaning="day, Sun", on_yomi="ニチ、ジツ", kun_yomi="ひ、ーぴ、ーか")
        response = self.client.get(reverse('api:kanji', args=('日',)))
        
        kanji_response_as_json = json.loads(response.content.decode('utf-8'))
        assert response.status_code == 200
        assert kanji_response_as_json.get("kanji") == '日'
        assert kanji_response_as_json.get("meaning") == "day, Sun"
        assert kanji_response_as_json.get("on_yomi") == "ニチ、ジツ"
        assert kanji_response_as_json.get("kun_yomi") == "ひ、ーぴ、ーか"
        

    # Test 404 response and no content returned with no Kanji
    def test_kanji_search_returns_404(self):
        response = self.client.get(reverse('api:kanji', args=('日',)))
        assert response.status_code == 404
        assert response.content == b'{}'


    def test_kanji_search_returns_400(self):
        response = self.client.get(reverse('api:kanji', args=('日曜日',)))
        assert response.status_code == 400
        assert response.content == b'{}'


    # Test 500 response returned if server error
    @patch('builtins.len')
    def test_kanji_search_returns_500(self, mock_corrupt_len):
        mock_corrupt_len.side_effect = Exception
        mock_request_argument = None
        response = get_kanji(mock_request_argument, '日')
        assert response.status_code == 500
        assert response.content == b'{}'
            

#class VocabFromJapaneseViewTests(TestCase):
    # Test 200 response given a word

    # Test 200 response given the furigana of the word

    # Test 404 response and no content returned

    # Test 500 response returned if server error


class VocabFromEnglishViewTests(TestCase):
    # Test 200 response given a word
    def test_vocab_search_using_english_returns_200(self):
        create_vocab(japanese_word="日", furigana="にち", english_word="Sun")
        response = self.client.get(reverse('api:vocab_from_english', args=("Sun",)))

        vocab_response_as_json = json.loads(response.content.decode('utf-8'))
        assert response.status_code == 200
        assert vocab_response_as_json.get("japanese_word") == "日"
        assert vocab_response_as_json.get("furigana") == "にち"
        assert vocab_response_as_json.get("english_word") == "Sun"


    # Test 404 response and no content returned
    def test_vocab_search_using_english_returns_404(self):
        response = self.client.get(reverse('api:vocab_from_english', args=("Sun",)))
        assert response.status_code == 404
        assert response.content == b'{}'


    # Test 500 response returned if server error
    @patch('API.models.Vocab.objects.filter')
    def test_vocab_search_using_english_returns_500(self, mock_corrupt_filter):
        mock_corrupt_filter.side_effect = Exception
        mock_request_argument = None
        response = get_vocab_using_english(mock_request_argument, 'Sun')
        assert response.status_code == 500
        assert response.content == b'{}'
