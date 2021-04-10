#Financial Analysis Code w/ Notes: Attachments- Budget_Data.csv
# The total number of months included in the dataset [x]
# The net total amount of "Profit/Losses" over the entire period [x]
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv

Budget_Data = os.path.join('Resources', 'Budget_Data.csv')

Months = []
months = 0
net = 0
net_change = []
netchange = 0
increase = 0 
decrease = 0

with open(Budget_Data) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
    
    first_row = next(reader)
    months += 1
    Months.append(months)
    net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:
        months += 1

        net += int(row[1])
        prev_net = int(first_row[1])
        
        if int(row[1]) > prev_net:
            netchange -= int(row[1])
            net_change.append(netchange)
            increase = netchange
        elif int(row[1]) < prev_net:
            netchange +=  int(row[1])
            net_change.append(netchange)
            decrease = int(netchange)
        else:
            continue
        Sum = round((sum(net_change)),4)
            
   
            
print ("Financial Analysis")
print("------------------------")
print (f"Total Months: {months}")
print (f"Total: ${net}")
print (f"Average Change: $-{Sum/286}")
print (f"Greatest Increase in Profits:{str(row[0])} ${int(row[1])}")
print (f"Greatest Decrease in Profits:{str(row[0])} $-{decrease}")
print("------------------------")

Final_Analysis = zip(Months, net_change)

#Set variable for output file
output_file = os.path.join("final_budgetanalysis.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Budget Analysis"])

    # Write in zipped rows
    writer.writerows(Final_Analysis)