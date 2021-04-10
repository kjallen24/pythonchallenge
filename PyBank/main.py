#Financial Analysis Code w/ Notes: Attachments- Budget_Data.csv
# The total number of months included in the dataset [x]
# The net total amount of "Profit/Losses" over the entire period [x]
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os #import systems
import csv# import csv

Budget_Data = os.path.join('Resources', 'Budget_Data.csv') #CSV to import

Months = []# holding variables and list
months = 0
sum_net = 0
prev_net = 0
net_change = []
netchange = 0
increase = 0 
decrease = 0

with open(Budget_Data) as financial_data:#open csv
    reader = csv.reader(financial_data)
    header = next(reader)
    
    first_row = next(reader)# skips the first row then add the first data row to count
    months += 1
    sum_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader: # continue to reads through the rest of the rows

        #first_row = next(reader) #function to move to next row
        Months.append(str(row[0])) #adds Months to list
        months += 1 # counts months
        sum_net += int(row[1]) # Sums the Profit/Losses
        net = int(row[1]) #holds value of net for each iteration
        next_net = int(first_row[1]) #holds value of net for next row
        
        if net > next_net: # evaluates whether current net is larger than next net
            netchange += (int(next_net - net)) # adds difference to variable
            net_change.append(netchange) # I thought I wanted it to preview in a list, couldn't figure it out so I didn't
            increase = str(row[0]), int(row[1]) # couldn't figure out how to grab this value for later
        elif net < next_net:
            netchange += (int(next_net - net))
            net_change.append(netchange)
            decrease = str(row[0]), int(row[1])
        else:
            continue
            
   
print("------------------------")           
print ("Financial Analysis")
print("------------------------")
print (f"Total Months: {months}")
print (f"Total: ${sum_net}")
print (f"Average Change: $-{netchange}")
print (f"Greatest Increase in Profits:{increase}")
print (f"Greatest Decrease in Profits:{decrease}")
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