import datetime
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from .models import DailySearchMetadata
from API.models import Kanji, Vocab
from API.views import EXPECTED_KANJI_QUERY_LENGTH, EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY

# Create your views here.
class SearchPageView(generic.DetailView):
    '''
    The main page for the TJED UI.
    '''
    template_name = 'ui/index.html'


class KanjiResultsPageView(generic.ListView):
    '''
    The view handling Kanji search results.
    '''
    template_name = 'ui/kanji_results.html'
    model = Kanji

    def get(self, request, kanji_character):
        '''
        The interfacing method for the UI when searching for Kanji.

        Parameters:
        ----------
        self : The object itself
        request : The request made by the end user
        kanji_character : The Kanji character in question

        Returns:
        ----------
            An HTTP response plus HTML, containing one of:
                200 -> Along with Kanji data
                400 -> Along with a response explaining why a bad request was made
                404 -> Along with a response explaining no Kanji exist for the query
                500 -> Along with a response explaining that there was an ISE
        '''
        try:
            # Update the Daily Search Metadata
            daily_search_metadata = DailySearchMetadata.objects.filter(date__exact=timezone.now()).first()
            if daily_search_metadata is None:
                daily_search_metadata = DailySearchMetadata.objects.create(date=timezone.now(), number_of_searches=0)
            daily_search_metadata.increment_searches()
            daily_search_metadata.save()

            # Return a "BAD REQUEST" given the Kanji query length is greater than 1
            if len(kanji_character) != EXPECTED_KANJI_QUERY_LENGTH:
                return render(request, 'ui/kanji_results.html', {
                    'error_message': "The query parameters provided were not of an appropriate length.",
                    'daily_search_metadata': daily_search_metadata
                }, status=400)

            # Return and render the kanji search results
            kanji = Kanji.objects.filter(kanji_character__exact=kanji_character)
            if len(kanji) < EXPECTED_NUMBER_OF_RESULTS_FROM_QUERY:
                return render(request, 'ui/kanji_results.html', {
                    'error_message': "No Kanji could be found via this search.",
                    'daily_search_metadata': daily_search_metadata
                }, status=404)
            else:
                return render(request, 'ui/kanji_results.html', {
                    'kanji_list': kanji,
                    'daily_search_metadata': daily_search_metadata
                }, status=200)
        except:
            return render(request, 'ui/server_error.html', {
                'error_message': "An issue occurred within the server"
            }, status=500)


class VocabResultsPageView(generic.ListView):
    '''
    The view handling Vocab search results.
    '''
    template_name = 'ui/vocab_results.html'
    model = Vocab

    def get(request, use_english_search, vocab):
        if use_english_search:
            return vocab_from_english(vocab)
        else:
            return vocab_from_japanese(vocab)

    def vocab_from_english(vocab):
        try:
            vocab_list = Vocab.objects.filter(english_word__startswith=vocab)
            if len(vocab_list) < 1:
                return render(request, 'ui/vocab_results.html', {
                    'error_message': "No Vocab could be found via the English term provided."
                }, status=404) # 404
            else:
                return render(request, 'ui/vocab_results.html', {
                    "vocab_list": vocab_list
                }, status=200) # 200
        except:
            return render(request, 'ui/server_error.html', {
                'error_message': "An issue occurred within the server"
            }, status=500) # 500

    def vocab_from_japanese(vocab):
        try:
            vocab_list = Vocab.objects.filter(japanese_word__contains=vocab)
            if len(vocab_list) < 1:
                vocab_list = Vocab.objects.filter(japanese_word__contains=vocab)
                if len(vocab_list) < 1:
                    return render(request, 'ui/vocab_results.html', {
                        'error_message': "No Vocab could be found via the Japanese term provided."
                    }, status=404)
                else:
                    return render(request, 'ui/vocab_results.html', {
                        "vocab_list": vocab_list
                    }, status=200) # 200
            else:
                return render(request, 'ui/vocab_results.html', {
                    "vocab_list": vocab_list
                }, status=200) # 200
        except:
            return render(request, 'ui/server_error.html', {
                'error_message': "An issue occurred within the server"
            }, status=500) # 500
