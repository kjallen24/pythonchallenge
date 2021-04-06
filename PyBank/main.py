#Financial Analysis Code w/ Notes: Attachments- Budget_Data.csv
# The total number of months included in the dataset []
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv

Budget_Data = os.path.join('Resources', 'Budget_Data.csv')
with open(Budget_Data, 'r') as f:
    budgetreader = csv.reader(f)
    print(budgetreader)
    for row in budgetreader:
        print (row)

