#Financial Analysis Code w/ Notes: Attachments- Budget_Data.csv
# The total number of months included in the dataset []
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv
import sys

Budget_Data = os.path.join('Resources', 'Budget_Data.csv')

def budgetanalysis(sheet):
    date = str(Budget_Data[0])
    prftlss = int(Budget_Data[1])
    total_net = count(str(Budget_Data))
    avgchng = average(str(Budget_Data))


with open(Budget_Data, 'r') as f:
    budgetreader = csv.reader(f)
    print(budgetreader)
    for column in budgetreader:
            print (column)
