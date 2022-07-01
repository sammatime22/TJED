from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class Kanji(models.Model):
    kanji_character = models.CharField(max_length=1, primary_key=True)
    meaning = models.CharField(max_length=100)
    on_yomi = models.CharField(max_length=100)
    kun_yomi = models.CharField(max_length=100)

    def __str__(self):
        kanji_to_return = self.kanji_character
        meaning_to_return = self.meaning
        on_yomi_to_return = self.on_yomi
        kun_yomi_to_return = self.kun_yomi
        kanji_as_json = {
            "kanji": kanji_to_return,
            "meaning": meaning_to_return,
            "on_yomi": on_yomi_to_return,
            "kun_yomi": kun_yomi_to_return
        }
        return str(kanji_as_json).replace("'", "\"")


class Vocab(models.Model):
    kanji = GenericRelation(Kanji)
    english_definition = models.CharField(max_length=100)
    japanese_definition = models.CharField(max_length=100)
