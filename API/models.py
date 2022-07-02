from django.db import models


class Kanji(models.Model):
    kanji_character = models.CharField(max_length=1, primary_key=True)
    meaning = models.CharField(max_length=100)
    on_yomi = models.CharField(max_length=100)
    kun_yomi = models.CharField(max_length=100)

    def __str__(self):
        return str({
            "kanji": self.kanji_character,
            "meaning": self.meaning,
            "on_yomi": self.on_yomi,
            "kun_yomi": self.kun_yomi
        }).replace("'", "\"")


class Vocab(models.Model):
    japanese_word = models.CharField(max_length=100)
    furigana = models.CharField(max_length=100)
    english_word = models.CharField(max_length=100)

    def __str__(self):
        if self.furigana is not None:
            return str({
                "japanese_word": self.japanese_word,
                "furigana": self.furigana,
                "english_word": self.english_word
            }).replace("'", "\"")
        else:         
            return str({
                "japanese_word": self.japanese_word,
                "english_word": self.english_word
            }).replace("'", "\"")
