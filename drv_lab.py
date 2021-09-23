#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Grace Michael
DS2500: Programming with Data

Created on Fri Mar  5 13:50:40 2021
@author: rachlin
"""

import random as rnd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns




class DRV:

    trials = 10000


    def __init__(self, dist = {}):
        """ Constructor """
        self.dist = dist


    def add_value(self, x, p):
        """ Add a value to the DRV with probability p """
        self.dist[x] = p

    def get_probability(self, x):
        """ Get the probability associated with the value x """
        return self.dist.get(x, 0)


    def random_value(self):
        """ return a random value in accordance with the DRV probability
        distribution """
        r = rnd.random()
        cumulp = 0.0
        for x in self.dist:
            cumulp += self.get_probability(x)
            if cumulp > r:
                return x

    def EV(self):
        """ Expected value (TODO) """
        EV = 0.0
        for (x,p) in self.dist.items():
            EV += x * p
        return EV


    def toDRV(self, vals):
        """ Convert a series of values to the corresponding discrete random variable """
        cnt = Counter(vals)
        total = sum(dict(cnt).values())
        dist = {x:c/total for (x,c) in dict(cnt).items()}
        return DRV(dist)


    def __add__(self, other):
        """ Add two discrete random variables (TODO: Support scalar) """
        return self.toDRV([self.random_value() + other.random_value() for i in range(DRV.trials)])

    def __radd__(self, a):
        """ Add a scalar, a, by the DRV """
        return self.toDRV([a + self.random_value() for i in range(DRV.trials)])


    def __sub__(self, other):
        """ Subtract two discrete random variables (TODO: Support scalar) """
        return self.toDRV([self.random_value() - other.random_value() for i in range(DRV.trials)])

    def __rsub__(self, a):
        """ Subtract two discrete random variables (TODO: Support scalar) """
        return self.toDRV([a - self.random_value() for i in range(DRV.trials)])


    def __mul__(self, other):
        """ Multiply two discrete random variables  """
        return self.toDRV([self.random_value() * other.random_value() for i in range(DRV.trials)])

    def __truediv__(self, other):
        """ Divide two discrete random variables (TODO: Support scalar) """
        return self.toDRV([self.random_value() / other.random_value() for i in range(DRV.trials)])


    def __rmul__(self, a):
        """ Multiply a scalar, a, by the DRV """
        return self.toDRV([a * self.random_value() for i in range(DRV.trials)])


    def __pow__(self, other):
        """ Multiply two discrete random variables (TODO: Support scalar) """
        return self.toDRV([self.random_value() ** other.random_value() for i in range(DRV.trials)])


    def __repr__(self):
        """ String representation of the DRV """

        xp = sorted(list(self.dist.items()))

        rslt = ''
        for x,p in xp:
            rslt += str(round(x)) + ' : '+ str(round(p,5)) + '\n'
        return rslt





    def plot(self, title='', xscale='', yscale='', trials=10000, bins=20, show_cumulative = True):
        """ Display the DRV distribution """

        sample = [self.random_value() for i in range(trials)]

        sns.displot(sample, kind='hist', stat='probability', bins=bins)
        plt.title(title)
        plt.xlabel('value')

        plt.grid()


        if xscale == 'log':
            plt.xscale(xscale)

        if yscale == 'log':
            plt.yscale(yscale)

        if show_cumulative:
            plt.yticks([0.0, 0.25, 0.50, 0.75, 1.00])
            xp = sorted(list(self.dist.items()))
            xval = [t[0] for t in xp]
            pval = [t[1] for t in xp]
            totalp = 0.0
            pcumul = []
            for p in pval:
                totalp += p
                pcumul.append(totalp)
            sns.lineplot(x=xval, y=pcumul)


def main():
    R = DRV({1.5:.25, 2.0:.25, 2.5:.25, 3.0:.25})
    # I wasn't sure what around 1 really meant
    fp = DRV({0.8:.03, 0.9:.07, 1.0:.80, 1.1:.07, 1.2:.03})
    n = DRV({1:.20, 2:.20, 3:.20, 4:.20, 5:.20})
    # Wikipedia estimates (Drake equation page)
    f_one = DRV({1:1, 0:0})
    fi = DRV({1:1, 0:0})
    fc = DRV({0.1:.50, 0.2:.50})
    # educated guesses based on wikipedia ranges
    L =DRV({1000:.46, 5000:.28, 10000:.13, 15000:.08, 100000:.05})
    N = R * fp * n * f_one * fi * fc * L
    N.plot(title='drake equation: civilizations',show_cumulative=False, trials=100000, yscale='log')
    plt.show()
    print('The expected number of civilizations is:', N.EV())

    # The expected number of civilizations is: 9453.6715


if __name__ == '__main__':
    main()
