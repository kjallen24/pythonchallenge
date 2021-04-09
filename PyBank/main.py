#Financial Analysis Code w/ Notes: Attachments- Budget_Data.csv
# The total number of months included in the dataset [x]
# The net total amount of "Profit/Losses" over the entire period [x]
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os
import csv

Budget_Data = os.path.join('Resources', 'Budget_Data.csv')

with open(Budget_Data) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)

    months = 0
    net = 0
    net_change = []
    greatest_increase = 0
    greatest_decrease = 0  
    
    first_row = next(reader)
    months += 1
    net += int(first_row[1])
    prev_net = first_row[1]

    for i, row in enumerate(reader):
        months += 1
        net += int(row[1])
        prev_net = int(row[1])
        diff = int(row[1]) - prev_net
        net_change.append(diff)
        print(diff)
       
        #average = net_change [] / 86
      
          
        
       # if prev_net > net_change[1]:
           # greatest_increase[0] = row [0]
            #greatest_increase[1] = net_change[1]
       # elif net_change < greatest_decrease[1]:
           # greatest_decrease[0] = row[0]
           # greatest_decrease[1] = net_change[1]
        #first_row += [1] 
        
        
    
print ("Financial Analysis")
print("------------------------")
print (f"Total Months: {months}")
print (f"Total: ${net}")
print (f"Average Change: ${average}")
#print (f"Greatest Increase in Profits:{greatest}")
#print (f"Greatest Decrease in Profits:{least}")
print("------------------------")

#Final_Analysis = zip(Date,TProfitLoss, PLAverage, Increase, Decrease)

# Set variable for output file
#output_file = os.path.join("final_analysis.csv")

#  Open the output file
#with open(output_file, "w", newline="") as datafile:
    #writer = csv.writer(datafile)

    # Write the header row
    #writer.writerow(["Financial Analysis"])

    # Write in zipped rows
    #writer.writerows(cleaned_csv)