### Our parsing script to gather Kanji data to place in TJED.
from bs4 import BeautifulSoup

# Constants used throughout the script
CHARACTER = "character" # Overarching character metadata
LITERAL = "literal" # The kanji_character
READING = "reading" # Overarching """Yomi""" tags or whatever
CLASS_ON_YOMI = "ja_on" # On Yomi
CLASS_KUN_YOMI = "ja_kun" # Kun Yomi
MEANING = "meaning" # English meaning

KANJI_CHARACTER_INDEX_TJED = 0
MEANING_INDEX_TJED = 1
ON_YOMI_INDEX_TJED = 2
KUN_YOMI_INDEX_TJED = 3

# Read in file and set up things
kanji_data_file = open("kanjidic2.xml", "r")
kanji_data_list = []
output_file = open("tjed_kanji.sql", "w")

# Gather data via BeautifulSoup, Get all character tags
soupy = BeautifulSoup(kanji_data_file.read())
character_tags = soupy.find_all(CHARACTER)

# for each character tag
for character_tag in character_tags:
    # gather the info and place it into the expected indicies
    kanji_data_list.append(gather_info_from_character_tag(character_tag))

# Write data out to file
for kanji_data in kanji_data_list:
    output_file.write("({} {} {} {})".format(kanji_data...))

# Helper methods
def gather_info_from_character_tag(character_tag_data):
    return []
