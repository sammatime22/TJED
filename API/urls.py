from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('kanji/<str:kanji_character>', views.get_kanji, name="kanji"),
    # path('vocab/japanese/<str:vocab>/', views.JapaneseToEnglishVocabView.as_view()),
    # path('vocab/english/<str:vocab>/', views.EnglishToJapaneseVocabView.as_view()),
]