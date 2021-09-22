"""
Grace Michael
DS2500: Programming with Data
HW 3
"""

import re
from collections import Counter
import matplotlib.pyplot as plt
import wordcloud as wc
import numpy as np
import pandas as pd
import seaborn as sns

STOPWORDS =["a", "an", "and", "the", "to", "i", "if", "of", "that", "it",
            "is", "im", "has", "was", "his", "ive", "at", "in", "your", "its",
            "for", "this", "but", "as", "are", "our", "we"]

def read(filename):
    # reads the txt file into a string
    string = open(filename, 'r').read()
    return string

def clean_speech(words):
    # splits the string into a list of lowercased words with no punctuation
    clean_words = []
    for word in words.split():
        word = re.sub("[^\w\s]", "", word)
        word = word.lower()
        if word not in STOPWORDS:
            clean_words.append(word)
    return clean_words

# positive and negative txt from https://github.com/jeffreybreen/twitter-sentiment-analysis-tutorial-201107/tree/master/data/opinion-lexicon-English
negative = read('negative.txt')
positive = read('positive.txt')
def score(speech):
    # the percentage of the speech that is positive and negative
    words = len(speech)
    neg_score = 0
    pos_score = 0
    for word in speech:
        if word in negative:
            neg_score = neg_score + 1
        if word in positive:
            pos_score = pos_score + 1
    neg_score = (neg_score / words) * 100
    # round to keep it clean
    neg_score = round(neg_score, 2)
    pos_score = (pos_score / words) * 100
    pos_score = round(pos_score, 2)
    return (neg_score, pos_score)

def word_cloud(speeches):
    # words list into a word cloud
    cloud = wc.WordCloud()
    word_cloud = cloud.generate(speeches)
    plt.axis('off')
    plt.imshow(word_cloud)
    plt.show()
    return plt

def most_common(speech):
    # counts the occurances of a word
    count = Counter(speech)
    # returns the 100 most common
    most_common = dict(count.most_common(100))
    return most_common

def sent_length(speech):
    count = []
    # separates speech by sentences
    sentence = speech.split(".")
    for sentences in sentence:
        # separates sentences into words
        words = sentences.split(' ')
        # counts words per sentence, adds count to list
        count.append(len(words))
    average = sum(count) / len(count)
    # rounds to 2 decimal places
    average = round(average, 2)
    return average

def avgwords_sentence(speech):
    #Average number of words of length > 6 per sentence
    count = []
    # separates speech by sentences
    sentence = speech.split(".")
    for sentences in sentence:
        # separates sentences into words
        words = sentences.split(' ')
        # filters out long enough words
        if len(words) >= 6:
            count.append(words)
    average = len(count) / len(sentence)
    # rounds to 2 decimal places
    average = round(average, 2)
    return average

def unique_words(speech):
    unique = []
    # add word if it isn't already added
    for word in speech:
        if word not in unique:
            unique.append(word)
    return len(unique)



def main():
    obama_string = read('obama2009.txt')
    clinton_string = read('clinton1993.txt')
    kennedy_string = read('kennedy1961.txt')
    ehower_string = read('eisenhower1953.txt')
    cool_string = read('coolidge1925.txt')
    bush_string = read('bush2001.txt')

    clean_obama = clean_speech(obama_string)
    clean_clinton = clean_speech(clinton_string)
    clean_kennedy = clean_speech(kennedy_string)
    clean_ehower = clean_speech(ehower_string)
    clean_cool = clean_speech(cool_string)
    clean_bush = clean_speech(bush_string)

    clean_obama_string = ' '.join(clean_obama)
    clean_clinton_string = ' '.join(clean_clinton)
    clean_kennedy_string = ' '.join(clean_kennedy)
    clean_ehower_string = ' '.join(clean_ehower)
    clean_cool_string = ' '.join(clean_cool)
    clean_bush_string = ' '.join(clean_bush)


    obama_cloud = word_cloud(clean_obama_string)
    clinton_cloud = word_cloud(clean_clinton_string)
    kennedy_cloud = word_cloud(clean_kennedy_string)
    ehower_cloud = word_cloud(clean_ehower_string)
    cool_cloud = word_cloud(clean_cool_string)
    bush_cloud = word_cloud(clean_bush_string)

    score_obama = score(clean_obama)
    score_clinton = score(clean_clinton)
    score_kennedy = score(clean_kennedy)
    score_ehower = score(clean_ehower)
    score_cool = score(clean_cool)
    score_bush = score(clean_bush)
    # turn scores into lists
    neg_list = [score_obama[0], score_clinton[0], score_kennedy[0], score_ehower[0], score_cool[0], score_bush[0]]
    pos_list = [score_obama[1], score_clinton[1], score_kennedy[1], score_ehower[1], score_cool[1], score_bush[1]]
    # labels
    names =['Obama', 'Clinton', 'Kennedy', 'Eisenhower', 'Coolidge', 'Bush']
    # scatterplot
    plt.scatter(neg_list, pos_list, color=['blue', 'blue', 'blue', 'red', 'red', 'red'])
    plt.title('Sentiment Analysis of Presidential Inaugural Addresses')
    plt.xlabel('Percent of Negative Speech')
    plt.ylabel('Percent of Positive Speech')
    for neg_list, pos_list, label in zip(neg_list, pos_list, names):
        # add the labels to the points
        plt.annotate(label, xy=(neg_list, pos_list), xytext=(7,0), textcoords='offset points', ha='left', va='center')
    plt.show()

    # 100 most common words in each speech
    mostcommon_obama = most_common(clean_obama)
    mostcommon_clinton = most_common(clean_clinton)
    mostcommon_kennedy = most_common(clean_kennedy)
    mostcommon_ehower = most_common(clean_ehower)
    mostcommon_cool = most_common(clean_cool)
    mostcommon_bush = most_common(clean_bush)

    # convert dictionaries to dataframes
    obama_df = pd.DataFrame(mostcommon_obama, index = ['Obama']).T
    clinton_df = pd.DataFrame(mostcommon_clinton, index = ['Clinton']).T
    kennedy_df = pd.DataFrame(mostcommon_kennedy, index = ['Kennedy']).T
    ehower_df = pd.DataFrame(mostcommon_ehower, index = ['Eisenhower']).T
    cool_df = pd.DataFrame(mostcommon_cool, index = ['Coolidge']).T
    bush_df = pd.DataFrame(mostcommon_bush, index = ['Bush']).T

    # make one dataframe, comparing to obama
    total_df = obama_df.join(clinton_df)
    total_df = total_df.join(kennedy_df)
    total_df = total_df.join(ehower_df)
    total_df = total_df.join(cool_df)
    total_df = total_df.join(bush_df)

    # plot as heatmap (show every word)
    sns.set(font_scale=.5)
    sns.heatmap(total_df, xticklabels=True, yticklabels=True)
    plt.title("Obama's Top 100 Common Words Among Other Presidential Inauguration Speeches")
    plt.xlabel('President')
    plt.ylabel('Words')
    plt.show()

    avg_obama = sent_length(obama_string)
    avg_clinton = sent_length(clinton_string)
    avg_kennedy = sent_length(kennedy_string)
    avg_ehower = sent_length(ehower_string)
    avg_cool = sent_length(cool_string)
    avg_bush = sent_length(bush_string)
    # labels
    names =['Obama', 'Clinton', 'Kennedy', 'Eisenhower', 'Coolidge', 'Bush']
    # data list
    length = [avg_obama, avg_clinton, avg_kennedy, avg_ehower, avg_cool, avg_bush]
    # bar chart
    plt.bar(names, length, color=['blue', 'blue', 'blue', 'red', 'red', 'red'])
    plt.title('Average Sentence Length of Presidential Inaugural Addresses')
    plt.xlabel('President')
    plt.ylabel('Average Sentence Length (in words)')
    plt.show()

    long_obama_avg = avgwords_sentence(obama_string)
    long_clinton_avg = avgwords_sentence(clinton_string)
    long_kennedy_avg = avgwords_sentence(kennedy_string)
    long_ehower_avg = avgwords_sentence(ehower_string)
    long_cool_avg = avgwords_sentence(cool_string)
    long_bush_avg = avgwords_sentence(bush_string)
    # labels
    names =['Obama', 'Clinton', 'Kennedy', 'Eisenhower', 'Coolidge', 'Bush']
    # data list
    length = [long_obama_avg, long_clinton_avg, long_kennedy_avg, long_ehower_avg, long_cool_avg, long_bush_avg]
    # bar chart
    plt.bar(names, length, color=['blue', 'blue', 'blue', 'red', 'red', 'red'])
    plt.title('Average Number of Long Words (> 6) per Sentence of Presidential Inaugural Addresses')
    plt.xlabel('President')
    plt.ylabel('Average Number of Long Words (> 6)')
    plt.show()

    obama_unique = unique_words(clean_obama)
    bush_unique = unique_words(clean_bush)
    clinton_unique = unique_words(clean_clinton)
    kennedy_unique = unique_words(clean_kennedy)
    ehower_unique = unique_words(clean_ehower)
    cool_unique = unique_words(clean_cool)
    bush_unique = unique_words(clean_bush)

    # labels
    years =['1925', '1953', '1961', '1993', '2001', '2009']
    # data list
    length = [cool_unique, ehower_unique, kennedy_unique, clinton_unique, bush_unique, obama_unique]
    # line chart
    plt.plot(years, length, marker='*', color="green")
    plt.title('Changes of the Number of Unique Words of Inaugural Address Over Time')
    plt.xlabel('Year of Address')
    plt.ylabel('Number of Unique Words')
    plt.show()



if __name__ == '__main__':
    main()
