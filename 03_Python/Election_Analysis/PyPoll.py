#the data we need to retrieve
# 1.The total number of votes cast
# 2.The complete list of voters who received votes
# 3. The percentage votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import csv
from datetime import datetime
import os  

file_to_load = os.path.join("Resources","election_results.csv")

file_to_save = os.path.join("analysis","election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    
    for row in file_reader:
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        total_votes += 1

print(total_votes)
print(candidate_options)
print(candidate_votes)

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes)*100

    print(f"{candidate_name}: received {vote_percentage:.1f}% of the total votes\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary =(
    f"-------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count {winning_count:,}\n"
    f"Winning Percentage {winning_percentage:.1f}%\n"
    f"-------------------------------\n")

print(winning_candidate_summary)




    






        


    

        

