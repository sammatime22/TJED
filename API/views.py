from .models import Kanji, Vocab

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render
from django.views import generic

# Constants associated with the Views of the API
EXPECTED_KANJI_QUERY_LENGTH = 1
EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY = 1
EMPTY_RESPONSE = "{}"


def get_kanji(request, kanji_character):
    try:
        if len(kanji_character) == EXPECTED_KANJI_QUERY_LENGTH:
            kanji = Kanji.objects.filter(kanji_character__exact=kanji_character)
            result_quantity = len(kanji)
            if result_quantity == EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY:
                return HttpResponse(kanji)
            elif result_quantity < EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY :
                return HttpResponseNotFound(EMPTY_RESPONSE)
            else:
                raise Exception("More than one entry found for same Kanji, " + kanji_character)
        else:
            return HttpResponseBadRequest(EMPTY_RESPONSE)
    except:
        return HttpResponseServerError(EMPTY_RESPONSE)


def get_vocab_using_japanese(request, japanese_word_query):
    try:
        vocab = Vocab.objects.filter(japanese_word__exact=japanese_word_query)
        if len(vocab) == EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY:
            return HttpResponse(vocab)
        else:
            vocab = Vocab.objects.filter(furigana__exact=japanese_word_query)
            if len(vocab) == EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY:
                return HttpResponse(vocab)
            else:
                return HttpResponseNotFound(EMPTY_RESPONSE)
    except:
        return HttpResponseServerError(EMPTY_RESPONSE)


def get_vocab_using_english(request, english_word_query):
    try:
        vocab = Vocab.objects.filter(english_word__exact=english_word_query)
        if len(vocab) == EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY:
            return HttpResponse(vocab)
        else:
            return HttpResponseNotFound(EMPTY_RESPONSE)
    except:
        return HttpResponseServerError(EMPTY_RESPONSE)
