"""
Grace Michael
DS2500: Programming with Data
Lab 3
"""

import re
import random

HAM = "hamilton_lyrics.txt"


#### TODO ####
# Update the read_lyrics function so it ignores everything in square brackets
# e.g., [HAMILTON], [ELIZA], [WHOLE COMPANY], etc.
#
# We also strongly suggest getting rid of punctuation!
def read_lyrics(filename):
    ''' Function: read_lyrics
        Parameters: filename, a string
        Returns: a list of strings, one string per line
                (removes empty lines and linebreaks,
                 and makes everything lowercase)
    '''
    all_lines = []
    final_lines = []
    #read file
    with open(filename) as infile:
        while True:
            line = infile.readline()
            if not line:
                break
            if line.strip() == "":
                continue
            all_lines.append(line.strip().lower())
            #get rid of all punctuation and labels
            for i in all_lines:
                x = re.sub(r'\[.,*!?\]', '', i)
                x = re.sub("[\(\[].*?[\)\]]", "", x)
                x = re.sub(r'[^\w\s]', '', x)
                final_lines.append(x)
    return final_lines

# lyrics lines from Hamilton
lyrics = read_lyrics("hamilton_lyrics.txt")
lyrics[:]=[y for y in lyrics if y]

# turn the lines into lists of words
words = ' '.join([str(lines) for lines in lyrics])
single_words = words.split()

# first word of line
begin = []
first = [0]
for i in lyrics:
    if len(lyrics) > 1:
        start = i.split()[0]
        begin.append(start)

# last or only word of line
end = []
last = [0]
for i in lyrics:
    if len(lyrics) >= 1:
        last = i.split()[-1]
        end.append(last)


# word (key) word that comes after (values)
dictionary = {}
first_word = ''
for word in single_words:
    if first_word not in dictionary:
        dictionary[first_word] = []
    dictionary[first_word].append(word)
    first_word = word

ngrams = dictionary


def generate_lyric(begin, ending, ngrams):
    '''
    Function: generate_lyric
        Parameters: list of begin-words, list of end-words,
                    dictionary of key = word, value = list of followed-by
        Returns: one line of Hamilton lyric
        '''

    sentence = ""
    curr_word = random.choice(begin)

    while True:
        sentence += " " + curr_word
        if curr_word in end:
            break
        curr_word = random.choice(ngrams[curr_word])
    return sentence

line = generate_lyric(begin, end, ngrams)
print(line)
