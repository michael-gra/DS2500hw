"""
Grace Michael
DS2500: Programming with Data
HW 5
"""

# Leaf Data
# This dataset was created by Pedro F. B. Silva and AndrÃ© R. S. MarÃ§al
# using leaf specimens collected by Rubim Almeida da Silva at the Faculty of Science, University of Porto, Portugal.
import pandas as pd
import numpy as np
from sklearn import datasets
from collections import Counter

# Load data
# create dataset
dataset = pd.read_csv('leaf.csv', header=None)
dataset.columns = ['Class', 'Specimen #', 'Eccentricity', 'Aspect Ratio', 'Elongation', 'Solidity', 'Stochastic Convexity',
'Isoperimetric Factor', 'Maximal Indentation Depth', 'Lobedness', 'Average Intensity', 'Average Contrast', 'Smoothness',
'Third Moment', 'Uniformity', 'Entropy']
dataset.head()









# x1 = test (Eccentricity)
# y1 = Class

# x2 = train

x1 = dataset.iloc[0][2]
y1 = dataset.iloc[0][0]


x2 = dataset[dataset.columns[2]].drop([0])
y2 = dataset[dataset.columns[0]].drop([0])

# KNN

class NearestNeighbor:

    def __init__(self, k):
        self.k = k

    def fit(self, x2, y2):
        self.x2 = x2
        self.y2 = y2

    def abs_difference(self, x, y):
        if x > y:
            return (x - y)
        else:
            return (y - x)

    def euc_distance(self, x, y):
        squaredistance = 0
        sumdistance = 0
        sqrtdistance = 0
        squaredistance = (self.abs_difference(x, y)) ** 2
        sumdistance += squaredistance
        sqrtdistance = sumdistance ** (1/2)
        return sqrtdistance

    def nearest(self, x1):
        test = [x1]
        for i in test:
            count = []
            length = []
            for j in range(len(self.x2)):
                dist = self.euc_distance(self.x2.iloc[j], x1)
                length.append([dist, j])
                length.sort()
                length = length[0:self.k]
        return length

    def score(self, x2):
        count = []
        nearest = self.nearest(x1)
        for data in nearest:
            row = data[1]
            print(row)
            # help fixing this
            class_num = dataset['Class'].iloc[0]
            print(class_num)
            if class_num == class_num:
                count.append(class_num)
                counted = Counter(count)
                most_common = counted.most_common(1)
                class_name = most_common[0][0]
        return class_name




def main():
# how to run for all of these (1,3,5,7,9,11,13,15,17....31)
    NN1 = NearestNeighbor(3)
    NN1.fit(x2, y2)
    print(NN1.nearest(x1))
    NN1.score(x2)

if __name__ == '__main__':
    main()

# what is overall accuracy cs weighted average precision. recal. f1-score for each k-values
# accuracy and classification report
# how many/what kind of visualizations
