from .models import Kanji, Vocab

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render
from django.views import generic

import json

# Constants associated with the Views of the API
EXPECTED_KANJI_QUERY_LENGTH = 1
EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY = 1
MAX_RESULTS_TO_RETUFN = 20
EMPTY_RESPONSE = "{}"


def get_kanji(request, kanji_character):
    '''
    Searches for data associated with a Kanji character.

    Parameters:
    ----------
    request : The request from the user
    kanji_character : The Kanji associated with the request

    Return:
    ----------
    A HTTP response, alongside Kanji data, if applicable.
    '''
    try:
        if len(kanji_character) == EXPECTED_KANJI_QUERY_LENGTH:
            kanji = Kanji.objects.filter(kanji_character__exact=kanji_character)
            result_quantity = len(kanji)
            if result_quantity == EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY:
                return HttpResponse(handle_array_as_json(kanji))
            elif result_quantity < EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY:
                return HttpResponseNotFound(EMPTY_RESPONSE)
            else:
                raise Exception("More than one entry found for same Kanji, " + kanji_character)
        else:
            return HttpResponseBadRequest(EMPTY_RESPONSE)
    except:
        return HttpResponseServerError(EMPTY_RESPONSE)


def get_vocab_using_japanese(request, japanese_word_query):
    '''
    Searches vocabulary, typically for the retrieval of the associated English word,
    provided the Japanese word.

    Parameters:
    ----------
    request : The request from the user
    japanese_word_query : The Japanese word associated with the request

    Return:
    ----------
    A HTTP response, alongside Vocab data, if applicable.
    '''
    try:
        vocab = Vocab.objects.filter(japanese_word__contains=japanese_word_query)
        if len(vocab) >= EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY:
            number_of_results_to_return = MAX_RESULTS_TO_RETUFN if len(vocab) > MAX_RESULTS_TO_RETUFN else len(vocab)
            return HttpResponse(handle_array_as_json(vocab[0:number_of_results_to_return]))
        else:
            vocab = Vocab.objects.filter(kana__contains=japanese_word_query)
            if len(vocab) >= EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY:
                number_of_results_to_return = MAX_RESULTS_TO_RETUFN if len(vocab) > MAX_RESULTS_TO_RETUFN else len(vocab)
                return HttpResponse(handle_array_as_json(vocab[0:number_of_results_to_return]))
            else:
                return HttpResponseNotFound(EMPTY_RESPONSE)
    except:
        return HttpResponseServerError(EMPTY_RESPONSE)


def get_vocab_using_english(request, english_word_query):
    '''
    Searches vocabulary, typically for the retrieval of the associated Japanese word,
    provided the English word.

    Parameters:
    ----------
    request : The request from the user
    english_word_query : The English word associated with the request

    Return:
    ----------
    A HTTP response, alongside Vocab data, if applicable.
    '''
    try:
        vocab = Vocab.objects.filter(english_word__startswith=english_word_query)
        if len(vocab) >= EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY:
            number_of_results_to_return = MAX_RESULTS_TO_RETUFN if len(vocab) > MAX_RESULTS_TO_RETUFN else len(vocab)
            return HttpResponse(handle_array_as_json(vocab[0:number_of_results_to_return]))
        else:
            return HttpResponseNotFound(EMPTY_RESPONSE)
    except:
        return HttpResponseServerError(EMPTY_RESPONSE)


def handle_array_as_json(terms_array):
    '''
    A helper method, which allows for an array of objects to be properly converted to JSON.
    
    Parameters:
    ----------
    terms_array : The terms in an array format

    Return:
    ----------
    A JSON array (as a string) of all of the terms, properly formatted
    '''
    formatted_terms_string = str(terms_array[0])
    if len(terms_array) > 1:
        for term in terms_array[1:len(terms_array)]:
            formatted_terms_string = formatted_terms_string + "," + str(term)
    return "[" + formatted_terms_string + "]"
