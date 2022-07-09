

urlpatterns = [
    url('<something>/kanji/<kanji_character>', ResultsPageView.kanji_search, 'kanji'),
    url('<something>/vocab/english/<vocab>', ResultsPageViewTests.english_vocab_search, 'eng_vocab'),
    url('<something>/vocab/japanese/<vocab>', ResultsPageViewTests.japanese_vocab_search, 'jpn_vocab')
]