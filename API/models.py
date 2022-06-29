from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class Kanji(models.Model):
    kanji_character = models.CharField(max_length=1, primary_key=True)
    meaning = models.CharField(max_length=100)
    on_yomi = models.CharField(max_length=100)
    kun_yomi = models.CharField(max_length=100)

    def __str__(self):
        kanji_as_json = {
            "kanji": self.kanji_character,
            "meaning": self.meaning,
            "on_yomi": self.on_yomi,
            "kun_yomi": self.kun_yomi
        }
        return str(kanji_as_json)


class Vocab(models.Model):
    kanji = GenericRelation(Kanji)
    english_definition = models.CharField(max_length=100)
    japanese_definition = models.CharField(max_length=100)
