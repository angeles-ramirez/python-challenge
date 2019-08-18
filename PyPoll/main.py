import os
import csv
from pathlib import Path 

total_cast_votes = 0
candidates = ["Khan", "Correy", "Li","O'Tooley"]
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0


input_file = Path("Resources", "election_data.csv")


with open(input_file,newline="",encoding="utf-8") as election:
    csv_reader = csv.reader(election,delimiter=",")
    header = next(csv_reader)

for row in csv_reader:
 
 ####* The total number of votes cast
    total_cast_votes +=1
  ####* A complete list of candidates who received votes

if row[2] == "Khan":
    khan_votes +=1
elif row[2] == "Correy":
    correy_votes +=1
elif row[2] == "Li": 
    li_votes +=1
elif row[2] == "O'Tooley":
    otooley_votes +=1

votes = [khan_votes, correy_votes,li_votes,otooley_votes]

dictionary_candidates_and_votes = dict(zip(candidates,votes))
winner = max(dictionary_candidates_and_votes, key=dictionary_candidates_and_votes.get)
  ####*  The percentage of votes each candidate won
khan_percent = (khan_votes/total_cast_votes) *100
correy_percent = (correy_votes/total_cast_votes) * 100
li_percent = (li_votes/total_cast_votes)* 100
otooley_percent = (otooley_votes/total_cast_votes) * 100
  ####* The total number of votes each candidate won
print(khan_votes)
print(correy_votes)
print(li_votes)
print(otooley_votes)

 #### * The winner of the election based on popular vote.

#### * As an example, your analysis should look similar to the one below:

  ####```text
  ####Election Results
 #### -------------------------
 #### Total Votes: 3521001
  ####-------------------------
  ####Khan: 63.000% (2218231)
  ####Correy: 20.000% (704200)
  ####Li: 14.000% (492940)
 #### O'Tooley: 3.000% (105630)
  ####-------------------------
 #### Winner: Khan
 #### -------------------------

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_cast_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")
####* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

output_file = Path("python-challenge", "PyPoll", "Election_Results_Summary.txt")

with open(output_file,"w") as file:

 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_cast_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"----------------------------")
