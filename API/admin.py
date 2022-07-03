from django.contrib import admin
from .models import Kanji, Vocab
# Register your models here.
admin.site.register(Kanji)
admin.site.register(Vocab)