from django.urls import path

from . import views

app_name = 'ui'
urlpatterns = [
    # also add in the index
    path('/search/kanji/<kanji_character>', views.KanjiResultsPageView.as_view(), 'kanji'),
    path('/search/vocab/english/<vocab>', views.VocabResultsPageView.as_view(), 'eng_vocab'),
    path('/search/vocab/japanese/<vocab>', veiws.VocabResultsPageView.as_view(), 'jpn_vocab')
]