from django.test import TestCase

# Create your tests here.
class KanjiViewTests(TestCase):
    # Test 200 response and content returned with available Kanji

    # Test 404 response and no content returned with no Kanji

    # Test 500 response returned if server error


class JapaneseToEnglishVocabViewTests(TestCase):
    # Test 200 response and content returned (definition, kanji and article link) provided Japanese word

    # Test 200 response and content returned (definition and kanji, but no article link) provided Japanese word

    # Test 404 response and no content returned

    # Test 500 response returned if server error


class EnglishToJapaneseVocabViewTests(TestCase):
    # Test 200 response and content returned (definition, kanji and article link) provided English word

    # Test 200 response and content returned (definition and kanji, but no article link) provided English word

    # Test 404 response and no content returned

    # Test 500 response returned if server error

