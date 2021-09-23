
'''
    DS2500
    Spring 2021
    OOP Lab - Runner Class
'''

import csv
from run import Run
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Runner:
    ''' Class to represent a runner.
        Attributes: name, color for the plot, marker shape for the plot (
                    strings)
        Methods: constructor is given.
        TODO: Create methods to get the data from a file,
              and to plot the runner's data'
    '''
    def __init__(self, name, color = "blue", marker = "o"):
        self.name = name
        self.color = color
        self.marker = marker
        self.runs = []

    def get_run_data(self, filename):
        with open(filename, 'r') as infile:
            csv_reader = csv.reader(infile, delimiter=',')
            next(csv_reader)
            for line in csv_reader:
                run = Run(float(line[0]),float(line[1]), float(line[2]))
                self.runs.append(run)


    def plot_run_dist(self):
        temp = [r.to_dict() for r in self.runs]
        run_df = pd.DataFrame([r.to_dict() for r in self.runs])
        sns.lineplot(data=run_df['dist'], color=self.color, marker=self.marker)
        plt.title('Runner Runs vs Distances')
        plt.xlabel('Run Number')
        plt.ylabel('Distance')
        plt.show()
