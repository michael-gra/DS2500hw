"""
Grace Michael
DS2500: Programming with Data
Lab 4
"""

import re
from collections import Counter
import matplotlib.pyplot as plt
import wordcloud as wc

SHEP = "shepard.txt"
BART = "bartlet.txt"
STOPWORDS =["a", "an", "and", "the", "to", "i", "if", "of", "that", "it",
            "is", "im", "has", "was", "his", "ive", "at", "in", "your", "its",
            "for", "this"]


def read(filename):
    string = open(filename, 'r').read()
    return string


def clean_speech(words):
    ''' Function: clean_speed
        Parameters: a string
        Returns: the string split into a list, but lowercased and
                 with punctuation removed,
                 and stopwords removed
    '''
    clean_words = []
    for word in words.split():
        word = re.sub("[^\w\s]", "", word)
        word = word.lower()
        if word not in STOPWORDS:
            clean_words.append(word)
    return clean_words

def mag(vec):
    ''' Function: mag
        Parameters: a vector (list of ints/floats)
        Returns: the magnitude of the vector
    '''
    mags = [num ** 2 for num in vec]
    return sum(mags) ** 0.5

def dot(v1, v2):
    ''' Function: dot
        Parameters: two vectors (list of ints/floats)
        Returns: the dot product of the vectors
    '''
    dots = [v1[i] * v2[i] for i in range(len(v1))]
    return sum(dots)

def compute_cosine(wc1, wc2):
    ''' Function compute_cosine
        Parameters: two dictionaries, with wordcounts
        Returns: a float, the cosine similarity measure
    '''

    # Start with all the words in both dictionaries, de-duped
    all_words = set(list(wc1.keys()) + list(wc2.keys()))

    # Make the vectors: 0 if they've never said the word,
    # the wordcount from given dictionary otherwise
    vec1 = {word : (wc1[word] if word in wc1.keys() else 0)
            for word in all_words}
    vec2 = {word : (wc2[word] if word in wc2.keys() else 0)
            for word in all_words}

    mag1 = mag(vec1.values())
    mag2 = mag(vec2.values())
    dot_prod = dot(list(vec1.values()), list(vec2.values()))
    return dot_prod / (mag1 * mag2)



def main():
    shepard = read(SHEP)
    bartlet = read(BART)

    uncleaned_shep_list = shepard.split()
    uncleaned_bart_list = bartlet.split()

    # cleaned
    shep_list = clean_speech(shepard)
    print(shep_list)
    bart_list = clean_speech(bartlet)

    cloud = wc.WordCloud()
    shep_cloud = cloud.generate(shepard)
    plt.axis('off')
    plt.imshow(shep_cloud)
    plt.show()
    cloud.to_file('shep.png')

    cloud = wc.WordCloud()
    bart_cloud = cloud.generate(bartlet)
    plt.axis('off')
    plt.imshow(bart_cloud)
    plt.show()
    cloud.to_file('bart.png')

    shep_count = Counter(shep_list)
    bart_count = Counter(bart_list)

    unclean_shep_count = Counter(uncleaned_shep_list)
    unclean_bart_count = Counter(uncleaned_bart_list)

    shep_count = dict(shep_count)
    bart_count = dict(bart_count)

    unclean_shep_count = dict(unclean_shep_count)
    unclean_bart_count = dict(unclean_bart_count)

    s_b_cos = compute_cosine(shep_count, bart_count)
    print("The cosine similarity of the cleaned data is", s_b_cos)
    # around what I expected from comparing the word clouds

    s_b_cos_unclean = compute_cosine(unclean_shep_count, unclean_bart_count)
    print("The cosine similarity of the uncleaned data is", s_b_cos_unclean)

    common_shep_count = Counter(shep_list).most_common(10)
    common_bart_count = Counter(bart_list).most_common(10)
    print('The 10 most common words of President Shepard are', common_shep_count)
    print('The 10 most common words of President Bartlet are',common_bart_count)
if __name__ == '__main__':
    main()
