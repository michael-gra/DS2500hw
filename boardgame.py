"""
Grace Michael
DS2500: Programming with Data
HW 1
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


# Part A: Read the Data into a Dictionary

def reading_boardgame_data(filename):
    bg_dict = {}
    # open and read file
    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            name = row[0]
            # filter for just solo games
            if int(row[1]) == 1:
                # create the nested dictionary
                bg_dict[name] = {}
                bg_dict[name]['minplaytime'] = float(row[2])
                bg_dict[name]['maxplaytime'] = float(row[3])
                bg_dict[name]['minage'] = float(row[4])
                bg_dict[name]['average'] = float(row[5])
                bg_dict[name]['avgweight'] = float(row[6])
    return bg_dict

# Part B: Make a Recommendation

def recommend(data, game):
    # no distance will be this big
    minimumdistance = 999999.9
    game_name = ''
    game_info = data[game]
    # first dictionary of game and it's info
    for key,value in data.items():
        # make sure same game is not returned
        if key != game:
            distance = euc_distance(game_info, value)
            # find smallest distance
            if distance < minimumdistance:
                minimumdistance = distance
                game_name = key
    return game_name

def euc_distance(game1, game2):
    key_sum = 0
    # nested dictionary of info categories and information
    for key, value in game1.items():
        key_sum += (value - game2[key]) ** 2
    distance = key_sum ** .5
    return distance

# Part C: Visualizations

# Barchart

def chart(data):

    # pull information from nested dictionaries
    avgrating = [data[game]['average'] for game in data]
    # round avg ratings for barchart
    avgrating_rounded = [round(x) for x in avgrating]

    # make array for Counter
    game_num = np.array(avgrating_rounded)
    number = Counter(game_num)
    # make lists to match eachother
    key = list(number.keys())
    value = list(number.values())

    # barchart information
    plt.bar(key, value, color='#DCD0FF')
    plt.title("Number of Games per Rating")
    plt.xlabel("Rating (rounded to nearest integer)")
    plt.ylabel("Number of Games")
    plt.show()

# Scatterplot

def plot(data):

    # pull information from nested dictionaries
    avgrating = [data[game]['average'] for game in data]
    gameweight = [data[game]['avgweight'] for game in data]

    # scatterplot information
    plt.title("Average User Rating vs Game Weight")
    plt.xlabel("Game Weight")
    plt.ylabel("Average User Rating")
    plt.grid()
    plt.scatter(gameweight, avgrating, marker='.', color='#301934')
    plt.show()

    # There appears to be a slight, positive correlation. As game weight increases,
    # the user rating looks to increase.


'''
# Part D: Business Marketing Thought Question

As the head of marketing for a boardgame company wishing to break into
the solo board gaming arena, I would recommend for the company to develop
a heavier boardgame. Though they may be more expensive to develop and manufacture,
the sales price will make it worth it, and the anticipated average user ratings will
encourage further sales, hence increasing profit. I would recommend for the target weight
to be between 3 and 5 pounds. This is because a majority of the boardgames in the scatterplot cluster
between 2 and 3 pounds with an average user rating ranging from about 2 all the way
to about 8.5. Heavier games, such as those in the 3 - 5 pound range are showing a
range of average user rating from about 4 to about 8.5 with a large cluster around a 7-8 rating.
This is a much more desirable range as lower rating scores are avoided. Future customers,
assuming they research their purchases, are more likely to purchase games with favorable reviews.
Because, according to this data, heavier games have more favorable reviews, it can be assumed
that they would be more likely purchased and positively reviewed. The more expensive games will also yield
a greater profit with fewer sales than more sales of a lighter, less expensive game.

'''

def main():
    data = reading_boardgame_data('bgg.csv')

    finalgame = recommend(data, 'Mage Knight Board Game')
    print(finalgame)

    barchart = chart(data)

    scatterplot = plot(data)


if __name__ == '__main__':
    main()
