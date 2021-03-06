from django.urls import path

from . import views

app_name = 'ui'
urlpatterns = [
    path('', views.SearchPageView.as_view(), name='index'),
    path('kanji/<str:kanji_character>', views.KanjiResultsPageView.as_view(), name='kanji'),
    path('vocab/japanese/<str:vocab>', views.VocabResultsPageView.as_view(), name='vocab_from_japanese'),
    path('vocab/english/<str:vocab>', views.VocabResultsPageView.as_view(), name='vocab_from_english'),
]
