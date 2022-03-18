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

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    for row in file_reader:
        print(row)

        

