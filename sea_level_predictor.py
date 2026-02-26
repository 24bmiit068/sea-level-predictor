# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 22:27:03 2026

@author: acer
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Line of best fit (ALL data)
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = range(1880, 2051)
    y_pred = res.intercept + res.slope * pd.Series(x_pred)
    plt.plot(x_pred, y_pred, 'r')

    # Line of best fit (from 2000)
    df_2000 = df[df["Year"] >= 2000]
    res2 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    x_pred2 = range(2000, 2051)
    y_pred2 = res2.intercept + res2.slope * pd.Series(x_pred2)
    plt.plot(x_pred2, y_pred2, 'green')

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()