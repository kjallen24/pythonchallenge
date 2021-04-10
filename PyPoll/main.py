#Election Results Code w/ Notes: Attachments- Election_Data.csv
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os # import operating system
import csv # import csv

Election_Data = os.path.join('Resources', 'Election_Data.csv') #CSV to import

candidates = [] #Empty list to collect candidate names

K_votes = 0 #hold variables for number of Votes per candidate
C_votes = 0
L_votes = 0
O_votes = 0

Kvote_per = 0 #hold variables for percentage of votes per candidate
Cvote_per = 0 
Lvote_per = 0 
Ovote_per = 0

vote_total = 0 #total number of votes

with open(Election_Data) as election_results: # open Election csv
    reader = csv.reader(election_results)
    header = next(reader) # skip first row

    for row in reader: # reads each row
        vote_total += 1 # for each row adds 1 to vote total

        if str(row[2]) not in candidates: 
            candidates.append(str(row[2])) # reads each line for candidate name and adds string to candidates [] if name is not there

        if candidates[0] in row[2]: # pulls each candidate name by pos. from list and counts vote
            K_votes += 1
        elif candidates[1] in row[2]:
            C_votes += 1
        elif candidates[2] in row[2]:
            L_votes += 1
        elif candidates[3] in row[2]:
            O_votes += 1
        else:
            continue

        votes = [K_votes, C_votes, L_votes, O_votes]
        
        Kvote_per = round(int(K_votes) / int(vote_total) * 100, 5) #calcs per of candidate vote, rounds to 5
        Cvote_per = round(int(C_votes) / int(vote_total) * 100, 5)
        Lvote_per = round(int(L_votes) / int(vote_total) * 100, 5)
        Ovote_per = round(int(O_votes) / int(vote_total) * 100, 5)

        vper = [Kvote_per, Cvote_per, Lvote_per, Ovote_per]

        if (K_votes > C_votes) and (K_votes > L_votes) and (K_votes > O_votes): #determines winner by comparing number of votes
            Winner = "Khan"
        elif (C_votes > K_votes) and (C_votes > L_votes) and (C_votes > O_votes):
            Winner = "Correy"
        elif (L_votes > K_votes) and (L_votes > C_votes) and (L_votes > O_votes):
            Winner = "Li"
        elif (O_votes > K_votes) and (O_votes > L_votes) and (O_votes > C_votes):
            Winner = "O'Tooley"
        else:
            continue

print("Election Results")
print("------------------------")
print(f"Total Votes: {vote_total}")
print("------------------------")
print(f"{candidates[0]}: {Kvote_per}%  ({K_votes})")
print(f"{candidates[1]}: {Cvote_per}%  ({C_votes})")
print(f"{candidates[2]}: {Lvote_per}%  ({L_votes})")
print(f"{candidates[3]}: {Ovote_per}%  ({O_votes})")
print("------------------------")
print(f"Winner: {Winner}")
print("------------------------")

Final_Analysis = zip(candidates,votes, vper)

# Set variable for output file
output_file = os.path.join("final_pollanalysis.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Poll Analysis: Total Votes"])

    # Write in zipped rows
    writer.writerows(Final_Analysis)