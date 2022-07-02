from .models import Kanji

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render
from django.views import generic

# Constants associated with the Views of the API
EXPECTED_KANJI_QUERY_LENGTH = 1
EXPECTED_NUMBER_OF_RESULTS_FROM_KANJI_QUERY = 1


def get_kanji(request, kanji_character):
    try:
        if len(kanji_character) == EXPECTED_KANJI_QUERY_LENGTH:
            kanji = Kanji.objects.filter(kanji_character__lte=kanji_character)
            result_quantity = len(kanji)
            if result_quantity == EXPECTED_NUMBER_OF_RESULTS_FROM_KANJI_QUERY:
                return HttpResponse(kanji)
            elif result_quantity < EXPECTED_NUMBER_OF_RESULTS_FROM_KANJI_QUERY :
                return HttpResponseNotFound('{}')
            else:
                raise Exception("More than one entry found for same Kanji, " + kanji_character)
        else:
            return HttpResponseBadRequest('{}')
    except:
        return HttpResponseServerError('{}')


#class JapaneseToEnglishVocabView():
    # Fill in info

#class EnglishToJapaneseVocabView():
    # Fill in info
