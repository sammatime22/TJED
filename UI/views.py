from django.shortcuts import render
from django.views import generic
from .models import DailySearchMetadata
from API.models import Kanji, Vocab

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

    def get(request, kanji_of_interest):
        # Update the Daily Search Metadata
        daily_search_metadata = DailySearchMetadata.objects.get(date=date)
        daily_search_metadata.increment_searches()
        daily_search_metadata.save()

        # Return and render the kanji sech results
        try:
            kanji = Kanji.objects.get(kanji_character__exact=kanji_of_interest)
            if len(kanji) < EXPECTED_KANJI_QUERY_LENGTH:
                return render(request, 'ui/kanji_results.html', {
                    'error_message': "No Kanji could be found via this search."
                }) # 404
            else:
                return render(request, 'ui/kanji_results.html', {
                    'kanji_list': kanji,
                    'daily_search_metadata': daily_search_metadata
                }) # 200
        except:
            return render(request, 'ui/server_error.html', {
                'error_message': "An issue occurred within the server"
            }) # 500


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
                }) # 404
            else:
                return render(request, 'ui/vocab_results.html', {
                    "vocab_list": vocab_list
                }) # 200
        except:
            return render(request, 'ui/server_error.html', {
                'error_message': "An issue occurred within the server"
            }) # 500

    def vocab_from_japanese(vocab):
        try:
            vocab_list = Vocab.objects.filter(japanese_word__contains=vocab)
            if len(vocab_list) < 1:
                vocab_list = Vocab.objects.filter(japanese_word__contains=vocab)
                if len(vocab_list) < 1:
                    return render(request, 'ui/vocab_results.html', {
                        'error_message': "No Vocab could be found via the Japanese term provided."
                    })
                else:
                    return render(request, 'ui/vocab_results.html', {
                        "vocab_list": vocab_list
                    }) # 200
            else:
                return render(request, 'ui/vocab_results.html', {
                    "vocab_list": vocab_list
                }) # 200
        except:
            return render(request, 'ui/server_error.html', {
                'error_message': "An issue occurred within the server"
            }) # 500
