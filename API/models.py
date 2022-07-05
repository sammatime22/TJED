from django.db import models


class Kanji(models.Model):
    '''
    Model representing Kanji, as well as attributes associated to said Kanji.

    Parameters:
    ----------
    kanji_character : The single character itself
    meaning : The meaning of the character
    on_yomi : The Sino-Japanese reading
    kun_yomi : The native Japanese reading
    '''
    kanji_character = models.CharField(max_length=1, primary_key=True)
    meaning = models.CharField(max_length=100)
    on_yomi = models.CharField(max_length=100)
    kun_yomi = models.CharField(max_length=100)

    def __str__(self):
        '''
        Returns a JSON string of the Kanji model.
        '''
        return str({
            "kanji": self.kanji_character,
            "meaning": self.meaning,
            "on_yomi": self.on_yomi,
            "kun_yomi": self.kun_yomi
        }).replace("'", "\"")


class Vocab(models.Model):
    '''
    A model representing both the Japanese and English word, along with assistance in reading the
    Japanese word if needed (kana).

    Parameters:
    ----------
    japanese_word : The Japanese word associated with the vocab
    kana (optional) : An assistance to reading the Japanese word
    english_word : The English word associated with the vocab
    '''
    japanese_word = models.CharField(max_length=20)
    kana = models.CharField(max_length=20)
    english_word = models.CharField(max_length=200)

    def __str__(self):
        '''
        Returns a JSON string of the Vocab model.
        '''
        if self.kana is not None:
            return str({
                "japanese_word": self.japanese_word,
                "kana": self.kana,
                "english_word": self.english_word
            }).replace("'", "\"")
        else:         
            return str({
                "japanese_word": self.japanese_word,
                "english_word": self.english_word
            }).replace("'", "\"")
