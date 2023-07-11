#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:12:19 2023

@author: sahar
"""



import pandas as pd
import matplotlib.pyplot as plt

# Change the path to the location of your CSV file
df = pd.read_csv('//Users/sahar/Documents/classes/Computational_material/HW3/result/All/T/All-T-time.csv', header=0, names=['Step', 'Temp1', 'Temp2', 'Temp3' ])

# Convert the 'step' column to time in seconds with an interval of 0.1 seconds
time = df['Step'] * 0.000001

# Get the pressure data from the 'pressure1' and 'pressure3' columns 

Temp1 = df['Temp1']
Temp2 = df['Temp2']
Temp3 = df['Temp3']


# Create a scatter plot of the pressure data against time
plt.figure(figsize=(5, 5), dpi=1200)
plt.plot(time, Temp1, label='Temperature step1', color='blue', linewidth=0.5)
plt.plot(time, Temp2, label='Temperature step2', color='red', linewidth=0.5)
plt.plot(time, Temp3, label='Temperature step3', color='green', linewidth=0.5)
plt.xlabel('Time [ns]', fontsize=14)
plt.ylabel('Temperature [K]', fontsize=14)
plt.title('Temperature vs Time', fontsize=12)


# Set the limits of the x and y axes
plt.xlim(0, 0.01)
plt.ylim(0, 300)

# Draw a line at y=0 in the middle of the plot
plt.axhline(y=0, color='black', linestyle='--')

plt.legend()
plt.tight_layout()
plt.show()