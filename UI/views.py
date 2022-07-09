from django.shortcuts import render
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

    def get(self, request):
        ...

    def kanji_search(self, kanji_of_interest):
        # Update the Daily Search Metadata
        daily_search_metadata = DailySearchMetadata.objects.get(date=date)
        daily_search_metadata.increment_searches()
        daily_search_metadata.save()

        # Return and render the kanji sech results
        try:
            kanji = Kanji.objects.get(kanji_character__exact=kanji_of_interest)
            if len(kanji) < EXPECTED_KANJI_QUERY_LENGTH:
                return render(404)
            else:
                return 200...
        except:
            return 500...


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
                return 404.....
            else:
                return 200
        except:
            return 500

    def vocab_from_japanese(vocab):
        try:
            vocab_list = Vocab.objects.filter(japanese_word__contains=vocab)
            if len(vocab_list) < 1:
                vocab_list = Vocab.objects.filter(japanese_word__contains=vocab)
                if len(vocab_list) < 1:
                    return 404
                else:
                    return 200
            else:
                return 200...
        except:
            return 500......
