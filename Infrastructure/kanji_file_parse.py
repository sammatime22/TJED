### Our parsing script to gather Kanji data to place in TJED.
from bs4 import BeautifulSoup
import os

# Constants used throughout the script
CHARACTER = "character" # Overarching character metadata
LITERAL = "literal" # The kanji_character
READING = "reading" # Overarching """Yomi""" tags or whatever
CLASS_ON_YOMI = "ja_on" # On Yomi
CLASS_KUN_YOMI = "ja_kun" # Kun Yomi
CLASS_ENG = "eng"
MEANING = "meaning" # English meaning

KANJI_CHARACTER_INDEX_TJED = 0
MEANING_INDEX_TJED = 1
ON_YOMI_INDEX_TJED = 2
KUN_YOMI_INDEX_TJED = 3

# Helper methods
def gather_attribute_string_from_items_list(items):
    item_list_string = ""
    item_list_length = len(items)
    items_viewed = 0
    for item in items:
        item_list_string = item_list_string + item.getText()
        items_viewed = items_viewed + 1
        if items_viewed < item_list_length:
            item_list_string = item_list_string + ", "
    return item_list_string.replace("\"", "")


def gather_info_from_character_tag(character_tag_data):
    kanji_character = character_tag_data.find(LITERAL).getText()
    on_yomi = gather_attribute_string_from_items_list(character_tag_data.find_all(READING, r_type=CLASS_ON_YOMI))
    kun_yomi = gather_attribute_string_from_items_list(character_tag_data.find_all(READING, r_type=CLASS_KUN_YOMI))
    meaning = gather_attribute_string_from_items_list(character_tag_data.find_all(MEANING, m_lang=CLASS_ENG))
    if meaning != "" and (on_yomi != "" or kun_yomi != ""):
        return [kanji_character, on_yomi, kun_yomi, meaning]


# Read in file and set up things
os.remove("tjed_kanji.sql")
kanji_data_file = open("kanjidic2.xml", "r")
kanji_data_list = []
output_file = open("tjed_kanji.sql", "w")

# Gather data via BeautifulSoup, Get all character tags
soupy = BeautifulSoup(kanji_data_file.read(), features='lxml')
character_tags = soupy.find_all(CHARACTER)

# for each character tag
for character_tag in character_tags:
    # gather the info and place it into the expected indicies
    character_tag_info = gather_info_from_character_tag(character_tag)
    if character_tag_info is not None:
        kanji_data_list.append(character_tag_info)

# Write data out to file
output_file.write("INSERT INTO API_kanji (kanji_character, on_yomi, kun_yomi, meaning) VALUES ")
number_of_kanji_entries = len(kanji_data_list)
number_of_kanji_entries_written = 0
for kanji_data in kanji_data_list:
    output_file.write("(\"{}\", \"{}\", \"{}\", \"{}\")".format(\
        kanji_data[KANJI_CHARACTER_INDEX_TJED], kanji_data[MEANING_INDEX_TJED],\
        kanji_data[ON_YOMI_INDEX_TJED], kanji_data[KUN_YOMI_INDEX_TJED]))
    number_of_kanji_entries_written = number_of_kanji_entries_written + 1
    if number_of_kanji_entries_written < number_of_kanji_entries:
        output_file.write(",\n")
    else:
        output_file.write(";")
