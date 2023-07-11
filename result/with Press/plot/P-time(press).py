#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:39:52 2023

@author: sahar
"""

import pandas as pd
import matplotlib.pyplot as plt

# Change the path to the location of your CSV file
df = pd.read_csv('//Users/sahar/Documents/classes/Computational_material/HW3/result/with Press/plot/P-time(press).csv', header=0, names=['Step', 'Press'])

# Convert the 'step' column to time in seconds with an interval of 0.1 seconds
time = df['Step'] * 0.000001

# Get the pressure data from the 'pressure1' and 'pressure3' columns
Press = df['Press']
#Pyy = df['Pyy']
#Pzz = df['Pzz']


# Create a scatter plot of the pressure data against time
plt.figure(figsize=(5, 5), dpi=1000)
plt.plot(time, Press, label='Press', color='blue', linewidth=0.5)
#plt.plot(time, Pyy, label='Pyy', color='red', linewidth=0.5)
#plt.plot(time, Pzz, label='Pzz', color='green', linewidth=0.5)
plt.xlabel('Time [ns]', fontsize=14)
plt.ylabel('Pressure [bar]', fontsize=14)
plt.title('Pressure vs Time ', fontsize=16)


# Set the limits of the x and y axes
plt.xlim(0, 0.011)
plt.ylim(-1000, 50000)

# Draw a line at y=0 in the middle of the plot
plt.axhline(y=0, color='black', linestyle='--')

plt.legend()
plt.tight_layout()
plt.show()