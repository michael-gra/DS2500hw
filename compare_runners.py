"""
Grace Michael
DS2500: Programming with Data
Lab 4
"""
import csv
from run import Run
from runner import Runner
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


RACHLIN = "rachlin.csv"
STRANGE = "strange.csv"


if __name__ == "__main__":

    # Instantiate two Runner objects so we can compare them
    rachlin = Runner("Rachlin", "green", "o")
    strange = Runner("Strange", "orange", "o")


    # Call the Runner method to read in the Runners' data
    rachlin.get_run_data(RACHLIN)
    strange.get_run_data(STRANGE)


    # Plot both runners' distance data
    plt.figure(1)
    rachlin.plot_run_dist()
    strange.plot_run_dist()


    # Optional but fun!!!!
    # Plot runners' paces histograms to compare
    # plt.figure(2)
    # plt.subplot(1, 2, 1)
    # rachlin.plot_histo()
    # plt.subplot(1, 2, 2)
    # strange.plot_histo()
