from django.db import models

# Create your models here.
class Kanji(models.Model):
    kanji_character = models.CharField(max_length=1)
    meaning = models.CharField(max_length=100)
    on_yomi = models.CharField(max_length=100)
    kun_yomi = models.CharField(max_length=100)


class Vocab(models.Model):
    kanji = models.ForeignKey(Kanji, on_delete=models.DO_NOTHING)
    english_definition = models.CharField(max_length=100)
    japanese_definition = models.CharField(max_length=100)
    example_sentence = models.ForeignKey(ExampleSentence, on_delete=models.DO_NOTHING)


class ExampleSentence(models.Model):
    example_sentence = models.CharField(max_length=200)
    english_translation_attempt = models.CharField(max_length=500)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class Article(models.Model):
    link = models.CharField(max_length=250)
