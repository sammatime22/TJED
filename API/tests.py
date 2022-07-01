from django.test import TestCase
from django.urls import reverse

from .models import Kanji, Vocab

import json

# Factory methods to facilitate testing
def create_kanji(kanji_character, meaning, on_yomi, kun_yomi):
    Kanji.objects.create(kanji_character=kanji_character, meaning=meaning, on_yomi=on_yomi, kun_yomi=kun_yomi)

def create_vocab(kanji, english_definition, japanese_definition):
    Vocab.objects.create(kanji=kanji, english_definition=english_definition, japanese_definition=japanese_definition)


# Create your tests here.
class KanjiViewTests(TestCase):
    # Test 200 response and content returned with available Kanji
    def test_kanji_search_returns_200(self):
        kanji_under_test = create_kanji(kanji_character='日', meaning="day, Sun", on_yomi="ニチ、ジツ", kun_yomi="ひ、ーぴ、ーか")
        response = self.client.get(reverse('api:kanji', args=('日',)))
        
        kanji_response_as_json = json.loads(response.content.decode('utf-8'))
        assert kanji_response_as_json.get("kanji") == '日'
        assert kanji_response_as_json.get("meaning") == "day, Sun"
        assert kanji_response_as_json.get("on_yomi") == "ニチ、ジツ"
        assert kanji_response_as_json.get("kun_yomi") == "ひ、ーぴ、ーか"
        

    # Test 404 response and no content returned with no Kanji

    # Test 500 response returned if server error


#class JapaneseToEnglishVocabViewTests(TestCase):
    # Test 200 response and content returned (definition, kanji and article link) provided Japanese word

    # Test 200 response and content returned (definition and kanji, but no article link) provided Japanese word

    # Test 404 response and no content returned

    # Test 500 response returned if server error


#class EnglishToJapaneseVocabViewTests(TestCase):
    # Test 200 response and content returned (definition, kanji and article link) provided English word

    # Test 200 response and content returned (definition and kanji, but no article link) provided English word

    # Test 404 response and no content returned

    # Test 500 response returned if server error

