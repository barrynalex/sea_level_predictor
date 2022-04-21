import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax=plt.subplots()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    year = np.linspace(1880,2050,171)
    pred = res.slope*year + res.intercept
    plt.plot(year, pred,'r')
    # Create second line of best fit
    new_df = df.loc[df['Year']>=2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    slope2, intercept2, r2, p2, se2 = linregress(new_x, new_y)
    year2 = np.linspace(2000,2050,51)
    pred2 = slope2*year2 + intercept2
    plt.plot(year2, pred2,'green')
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()