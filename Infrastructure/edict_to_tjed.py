### edict_to_tjed.py
### This is an infrastructure resource used to convert a publicly available 
### edict.sql file (for EDICT, thank you Kyle Hasegawa!) to the TJED format.
### NOTE that this is just for the Vocab table.

# Constants used throughout this file
JAPANESE_WORD_INDEX_TJED = 0
JAPANESE_KANA_INDEX_TJED = 1
ENGLISH_WORD_INDEX_TJED = 2

# Read lines
edict_source_file = open("edict.sql", "r")
edict_source_file_lines = edict_source_file.readlines()
tjed_destination_file = open("tjed.sql", "w")
tjed_destination_file_lines = []

# for each line
for line in edict_source_file_lines:
    # if it is a line we shouldn't skip
    if not should_skip(line):
        # cut out the parts
        line_parts = cut_line_parts(line)
        # if the word portion is empty
        if line_parts[JAPANESE_WORD_INDEX_TJED] == '':
            # the kana portion is the word portion, and the kana portion is empty
            line[JAPANESE_WORD_INDEX_TJED] = line[JAPANESE_KANA_INDEX_TJED]
        tjed_destination_file_lines.append(line_parts)

# write lines
...
for line_parts in tjed_destination_file_lines:
    tjed_destination_file.write("({}, {}, {})".format(tjed_destination_file_lines))
...

def should_skip(line):
    return False

def cut_line_parts(line):
    return []
