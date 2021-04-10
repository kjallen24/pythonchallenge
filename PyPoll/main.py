#Election Results Code w/ Notes: Attachments- Election_Data.csv
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

Election_Data = os.path.join('Resources', 'Election_Data.csv')

votes = 0
candidates = ["Correy", "Khan", "Li", "O'Tooley"]
vote_per = 0 
vote_total = 0

with open(Election_Data) as election_results:
    reader = csv.reader(election_results)
    header = next(reader)

    for row in reader:
        votes += 1
        if candidates[0] in row[2]:
            C_votes += 1
        elif candidates[1] in row[2]:
            K_votes += 1
        elif candidates[2] in row[2]:
            L_Votes += 1
        elif candidates[3] in row[2]:
            O_Votes += 1
        else:
            continue

print(votes)
print(C_votes)
        

        