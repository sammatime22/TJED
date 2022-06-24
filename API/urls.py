from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('kanji/<str:pk>/', views.KanjiView.as_view()),
    path('vocab/japanese/<str:vocab>/<bool:include_example>/', views.JapaneseToEnglishVocabView.as_view()),
    path('vocab/english/<str:vocab>/<bool:include_example>/', views.EnglishToJapaneseVocabView.as_view()),
]