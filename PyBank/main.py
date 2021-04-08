#Financial Analysis Code w/ Notes: Attachments- Budget_Data.csv
# The total number of months included in the dataset []
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv

Budget_Data = os.path.join('Resources', 'Budget_Data.csv')

with open(Budget_Data, 'r') as csvfile:
    cvsreader = csv.reader(csvfile, delimiter=',')
    lines = len(list(cvsreader))
    print (lines-1)

#Final_Analysis = zip(Date,TProfitLoss, PLAverage, Increase, Decrease)

# Set variable for output file
#output_file = os.path.join("final_analysis.csv")

#  Open the output file
#with open(output_file, "w", newline="") as datafile:
    #writer = csv.writer(datafile)

    # Write the header row
    #writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     #"Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    #writer.writerows(cleaned_csv)