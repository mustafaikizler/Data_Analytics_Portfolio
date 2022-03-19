#the data we need to retrieve
# 1.The total number of votes cast
# 2.The complete list of voters who received votes
# 3. The percentage votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import csv
from datetime import datetime
import os  

#Assign a variable to load a file from the path
file_to_load = os.path.join("Resources","election_results.csv")

#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

#initiliza a total vote counter(started with 0)
total_votes = 0
#candidate options and candidate votes(for 3 candidates creeated a list, also we will call the total candidate votes by name via dict.)
candidate_options = []
candidate_votes = {}

#Track the winning candidate(str),votes count(int) and winning percentage(float)
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election result and read the file with the csv.reader.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read the header row and skip the header with the NEXT.
    headers = next(file_reader)

    #Print each row in the csv file (iterat)
    for row in file_reader:
        #add the total value count in every row adds 1 votes (except header because we already skipped with next)
        total_votes += 1
        #gets the candidate name for each row, candidate name in 3rd column or second index and stores there 
        candidate_name = row[2]
        #we will store the candidate names in candidate options, however there are only 3 different candidate name thats why we gonna-
        #all 3 unqie candidates 
        if candidate_name not in candidate_options:
            #Adds the candidate names in a candidate options list
            candidate_options.append(candidate_name)
            #we get the candidate votes according to candidate name because candidate name is key, and value is votes 
            candidate_votes[candidate_name] = 0
        else:
            #adds a vote to that candidate's count
            candidate_votes[candidate_name] += 1

#saves the results to our text file.
with open(file_to_save,"w") as txt_file:
    #here prints the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")
    
    # After printing the final vote count to the terminal save the final vote count to the text file
    txt_file.write(election_results)

    print(total_votes)
    print(candidate_options)
    print(candidate_votes)


    for candidate_name in candidate_votes:
        #after election results 
        #a = {"Mike" = 1, "mustafa" = 2, "burak" = 4}
        #Candidate name is the key,  is represents the vote count
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100

        print(f"{candidate_name}: received {vote_percentage:.1f}% of the total votes\n")

        

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        #Determine winning candidates,winning vote count, and winning percentage.
        #every candidatess information is going to be equal to winning count, at the end if the existing one is the largest one it-
        #becomes winning count, percentage or count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                    winning_count = votes
                    winning_percentage = vote_percentage
                    winning_candidate = candidate_name
    #writes winning candidates to the terminal
    winning_candidate_summary =(
        f"-------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count {winning_count:,}\n"
        f"Winning Percentage {winning_percentage:.1f}%\n"
        f"-------------------------------\n")
    print(winning_candidate_summary)

    #Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)







    






        


    

        

