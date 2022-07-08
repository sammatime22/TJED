### edict_to_tjed.py
### This is an infrastructure resource used to convert a publicly available 
### edict.sql file (for EDICT, thank you Kyle Hasegawa!) to the TJED format.
### NOTE that this is just for the Vocab table.
import os
import re

# Constants used throughout this file
JAPANESE_WORD_INDEX_TJED = 0
JAPANESE_KANA_INDEX_TJED = 1
ENGLISH_WORD_INDEX_TJED = 2

JAPANESE_WORD_INDEX_EDICT = 1
JAPANESE_KANA_INDEX_EDICT = 2
ENGLISH_WORD_INDEX_EDICT = 3


# Helper Functions
def cut_line_parts(line):
    line_parts = line[1:-3].split(",'")
    japanese_word = line_parts[JAPANESE_WORD_INDEX_EDICT].replace("'", "")
    japanese_kana = line_parts[JAPANESE_KANA_INDEX_EDICT].replace("'", "")
    english_word_parts = line_parts[ENGLISH_WORD_INDEX_EDICT]\
                            .replace("'", "").replace("/(P)", "")\
                            .replace("(n)", "").replace("/", ", ")\
                            .replace("\s", "'s").replace("\\\"", "").split(" ")

    english_word = ""
    for i in range(1, len(english_word_parts)):
        english_word += " " + english_word_parts[i]

    return [japanese_word, japanese_kana, english_word[1:]]

# START
# Read lines
os.remove("tjed_vocab.sql")
edict_source_file = open("edict_modified.sql", "r")
edict_source_file_lines = edict_source_file.readlines()
tjed_destination_file = open("tjed_vocab.sql", "w")
tjed_destination_file_lines = []
banned_words_file = open("banned_words.txt", "r")
banned_words = banned_words_file.readlines()

# for each line
for line in edict_source_file_lines:
    # cut out the parts, add it to the lines to append to the destination file
    line_parts = cut_line_parts(line)
    if line_parts is not None:
        contained_banned_word = False
        for word in banned_words:
            if line_parts[ENGLISH_WORD_INDEX_TJED].__contains__(" " + word[:-1] + ",")\
                or line_parts[ENGLISH_WORD_INDEX_TJED].__contains__(" " + word[:-1] + " ")\
                or line_parts[ENGLISH_WORD_INDEX_TJED].__contains__(" " + word[:-1])\
                or line_parts[ENGLISH_WORD_INDEX_TJED].split(",")[0] == word[:-1]\
                or line_parts[ENGLISH_WORD_INDEX_TJED].split(" ")[0] == word[:-1]:
                contained_banned_word = True
                break

        if not contained_banned_word:
            tjed_destination_file_lines.append(line_parts)

# write lines
tjed_destination_file.write('INSERT INTO API_vocab (japanese_word, kana, english_word) VALUES\n')
lines_to_write = len(tjed_destination_file_lines) - 1
lines_written = 0
for line_parts in tjed_destination_file_lines:
    tjed_destination_file.write("(\"{}\", \"{}\", \"{}\")"\
        .format(line_parts[JAPANESE_WORD_INDEX_TJED],\
                line_parts[JAPANESE_KANA_INDEX_TJED],\
                line_parts[ENGLISH_WORD_INDEX_TJED]))
    if lines_written < lines_to_write:
        tjed_destination_file.write(",\n")
        lines_written += 1
    else:
        tjed_destination_file.write(';')
