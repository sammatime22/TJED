from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('kanji/<str:kanji_character>/', views.get_kanji, name="kanji"),
    path('vocab/japanese/<str:japanese_word_query>/', views.get_vocab_using_japanese, name="vocab_from_japanese"),
    path('vocab/english/<str:english_word_query>/', views.get_vocab_using_english, name="vocab_from_english"),
]
