#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 12:10:20 2023

@author: sahar
"""

import pandas as pd
import matplotlib.pyplot as plt

# Change the path to the location of your CSV file
df = pd.read_csv('//Users/sahar/Documents/classes/Computational_material/HW3/result/data/Step_Energy.csv', header=0, names=['Step', 'TotEng'])

# Convert the 'step' column to time in seconds with an interval of 0.1 seconds
time = df['Step'] * 0.000001

# Get the pressure data from the 'pressure1' and 'pressure3' columns
TotEngh = df['TotEng']
#Pyy = df['Pyy']
#Pzz = df['Pzz']


# Create a scatter plot of the pressure data against time
plt.figure(figsize=(5, 5), dpi=1000)
plt.plot(time, TotEng, label='TotEng', color='blue', linewidth=0.5)
#plt.plot(time, Pyy, label='Pyy', color='red', linewidth=0.5)
#plt.plot(time, Pzz, label='Pzz', color='green', linewidth=0.5)
plt.xlabel('Time [ns]', fontsize=14)
plt.ylabel('Energy [eV]', fontsize=14)
plt.title('Energy vs Time ', fontsize=16)


# Set the limits of the x and y axes
plt.xlim(0, 0.011)
plt.ylim(38500, 39500)

# Draw a line at y=0 in the middle of the plot
plt.axhline(y=0, color='black', linestyle='--')

plt.legend()
plt.tight_layout()
plt.show()