# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:37:15 2023

@author: sigma
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the Excel file
excel_file = pd.ExcelFile('D:\Derivatives Trading\TAIEX derivatives trading record.xlsx')

# Get the sheet you want to read
sheet_name = 'ForPython' # Replace with the name of the sheet you want to read
df = excel_file.parse(sheet_name)

# Output data information
print(df.head())

#******Plotting setup*****#
# Generate some data
Date = df["Date"]
Date
y1 =df["PnL Index"]
y1
y2 = df["TAIEX"]
y2

# Create the plot and set the first y-axis (left)
fig, ax1 = plt.subplots()
plt.xticks(rotation=90)
ax1.plot(Date, y1, 'b-')
ax1.set_xlabel('Date')
ax1.set_ylabel('PnL Index (Base = 100)', color='b')
ax1.tick_params('y', colors='b')

# Set the second y-axis (right)
ax2 = ax1.twinx()
ax2.plot(Date, y2, 'k.')
ax2.set_ylabel('TAIEX', color='k')
ax2.tick_params('y', colors='k')

# Show the plot
plt.title('PnL vs TAIEX')
plt.show()


#Pnl vs VIX
y3 = df["VIX"]
y3

# Create the plot and set the first y-axis (left)
fig, ax1 = plt.subplots()
plt.xticks(rotation=90)
ax1.plot(Date, y1, 'b-')
ax1.set_xlabel('Date')
ax1.set_ylabel('PnL Index (Base = 100)', color='b')
ax1.tick_params('y', colors='b')

# Set the second y-axis (right)
ax3 = ax1.twinx()
ax3.plot(Date, y3, 'm.')
ax3.set_ylabel('VIX', color='m')
ax3.tick_params('y', colors='m')

# Show the plot
plt.title('PnL vs VIX')
plt.show()

#Sharpe ratio
# Read in the portfolio returns data from a CSV file
R_first=df["PnL Index"].iloc[0,]
R_first
R_last=df["PnL Index"].iloc[165,]  #Always excel's actual row-2
R_last

portfolio_returns=(R_last-R_first)/R_first
portfolio_returns


daily_returns=df["Returns"]
daily_returns


# Calculate the excess returns and standard deviation
risk_free_rate = 0.0145  # Taiwan savings rate
excess_returns = portfolio_returns - risk_free_rate
std_dev = np.std(daily_returns)
print("Standard Deviation of Daily Return:", std_dev)
# Calculate the Sharpe ratio
sharpe_ratio = excess_returns / std_dev

print("Sharpe Ratio:", sharpe_ratio)
