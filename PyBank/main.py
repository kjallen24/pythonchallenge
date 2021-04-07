#Financial Analysis Code w/ Notes: Attachments- Budget_Data.csv
# The total number of months included in the dataset []
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv

Budget_Data = os.path.join('Resources', 'Budget_Data.csv')

def budgetanalysis(Budget_Data):

    date = str(Budget_Data[0])
    prftlss = int(Budget_Data[1])
    ttlmonths = len(list(Budget_Data[0]))
    avgchng = average(str(Budget_Data[0]))
    for column in budgetreader:
        print (ttlmonths)

print(ttlmonths)

with open(Budget_Data, 'r') as f:
    budgetreader = csv.reader(f)
    header = next(budgetreader)
    print(budgetreader)

