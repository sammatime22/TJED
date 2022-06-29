from .models import Kanji

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
def get_kanji(request, kanji_character):
    kanji = get_object_or_404(Kanji, pk=kanji_character)
    try:
        return HttpResponse(kanji)
    except:
        return None

#class JapaneseToEnglishVocabView():
    # Fill in info

#class EnglishToJapaneseVocabView():
    # Fill in info
