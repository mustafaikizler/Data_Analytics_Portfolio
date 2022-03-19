# Colorado Board Election Analysis
## Overview of Election Audit
Our main purpose was the processing the raw data of the Colorado elections. Raw data received in CSV file, in order the manipulate the data we used programming language Python and interpreter VS Code. By using these tools we prepared a report in a text file that contains:
- Overall Election results
- Results for Counties
- Results for Candidates
- Winner of the Election
- variatey of stats belongs to counties and candidates.
## Election Audit Results
- Total Votes :        369,711
- County Votes:
  - Jefferson: 10.5%  
    votes:  38,855
  - Denver: 82.8%    
    votes:    306,055
  - Arapahoe: 6.7%   
    votes:    24,801
- Denver has the largest  number of votes.
- Candidate Results
   - Charles Casper Stockham: 23.0%,
    votes 85,213
   - Diana DeGette: 73.8%, 
    votes 272,892
   - Raymon Anthony Doane: 3.1%,
     votes 11,606
 - Winner of the Election
   - Winner: Diana DeGette
   - Winning Vote Count: 272,892
   - Winning Percentage: 73.8%
## Election-Audit Summary
### The base code
Short Explanations are written ☑️xyz☑️ in order to understand the logic of the code script. 
'''

                 ☑️ create a path from raw data and to txt file ☑️
                  file_to_load = os.path.join("Resources", "election_results.csv")            
                  file_to_save = os.path.join("analysis", "election_analysis.txt")
                  
                  ☑️Identify the variables that hold the results☑️  
                  total_votes = 0                  
                  candidate_options = []
                  candidate_votes = {}
               
                  county_options = []
                  county_votes = {}

                  
                  winning_candidate = ""
                  winning_count = 0
                  winning_percentage = 0
                 
                  largest_turnout_county = ""
                  largest_turnout_county_votes = 0
                  
                  ☑️Open and read the CSV file☑️☑
                  with open(file_to_load) as election_data:
                      reader = csv.reader(election_data)
                      ☑️Skip the Heading☑️
                      header = next(reader)
                     
                      for row in reader:
                                                
                          total_votes = total_votes + 1
                         
                         ☑️Get the candidate name (the third column in CSV file☑️
                          candidate_name = row[2]
                         ☑️Get the County name (the second column in CSV file ☑️
                          county_name = row[1]                       
                          
                          if candidate_name not in candidate_options:
                          
                             ☑️candidate name to the variable ☑️
                              candidate_options.append(candidate_name)
                              
                              ☑️Identify the variables that hold the results☑️
                              candidate_votes[candidate_name] = 0
                      
                         candidate_votes[candidate_name] += 1
                        
                          if county_name not in county_options:
                              
                              county_options.append(county_name)
                              
                              ☑️Identify the variables that hold the results☑️
                              county_votes[county_name] = 0
                          ☑️collect the each county votes according to county name in dictionary☑️
                          county_votes[county_name] += 1
                 
                 ☑️Print the ELection results to text file☑️
                  with open(file_to_save, "w") as txt_file:
                     
                      election_results = (
                          f"\nElection Results\n"
                          f"-------------------------\n"
                          f"Total Votes: {total_votes:,}\n"
                          f"-------------------------\n\n"
                          f"County Votes:\n")
                      print(election_results, end="")

                      txt_file.write(election_results)
                     
                     ☑️County results☑️
                      for county_name in county_votes:
                          
                          ☑️find county votes according to county name in dictionary☑️
                          cvotes = county_votes[county_name]
                          
                         ☑️calculate percentage☑️
                          cvotes_percentage = float(cvotes)/float(total_votes)*100                          
                          print(
                              f"County Votes\n"
                              f"{county_name}: {cvotes_percentage:.1f}% ({cvotes:,})\n")   
                          county_results = (f"{county_name}: {cvotes_percentage:.1f} ({cvotes:,})\n")                        
                          txt_file.write(county_results)
                          
                          ☑️Find the largers county by vote number and county name ☑️
                          if cvotes > largest_turnout_county_votes:
                              largest_turnout_county = county_name
                              largest_turnout_county_votes = cvotes
                      
                      print(
                          f"-----------------------------------------\n"
                          f"Largest County Turnout: {largest_turnout_county}\n"
                          f"--------------------------------------------\n")
                      largest_county =(
                          f"-----------------------------------------\n"
                          f"Largest County Turnout: {largest_turnout_county}\n"
                          f"--------------------------------------------\n") 

                      txt_file.write(largest_county)
                    
                      for candidate_name in candidate_votes:
                          
                          votes = candidate_votes.get(candidate_name)
                          vote_percentage = float(votes) / float(total_votes) * 100
                          candidate_results = (
                              f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                          
                          print(candidate_results)
                          #  Save the candidate results to our text file.
                          txt_file.write(candidate_results)
                         
                         ☑️Find the winning candidare by vote number and county name name ☑️
                          if (votes > winning_count) and (vote_percentage > winning_percentage):
                              winning_count = votes
                              winning_candidate = candidate_name
                              winning_percentage = vote_percentage
                     
                      winning_candidate_summary = (
                          f"-------------------------\n"
                          f"Winner: {winning_candidate}\n"
                          f"Winning Vote Count: {winning_count:,}\n"
                          f"Winning Percentage: {winning_percentage:.1f}%\n"
                          f"-------------------------\n")
                      print(winning_candidate_summary)
                     
                      txt_file.write(winning_candidate_summary)
'''
### How Can We Modify The Code In Order To Use For Future Elections?

- Every election has its own unique CSV file. First of all we need to correct paths to raw data and target txt file ⬇️

![path](https://user-images.githubusercontent.com/98247252/159135372-6bd75d6c-2678-4b39-a065-79955b8af3df.png)

- New CSV file might have different sequence and much more column and row. First we need to review the data. 
- After, we can identify the index number of the data that we want to store in a variable. That requires to modify index numbers in the code as well. ⬇️



![index](https://user-images.githubusercontent.com/98247252/159135485-a8a192e1-3da4-48ff-9ab2-38b18d30725b.jpg)





    


 
 


