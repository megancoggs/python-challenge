# PyPoll Challenge

# Import modules
import os
import csv

# Create empty lists for each column in the dataset
voter_list = []
county_list = []
candidate_list = []

# Set path
csv_path = os.path.join("resources", "election_data.csv")

with open(csv_path) as csvfile:

    # Create object to read csv file
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row
    header = next(csvreader)

    # Loop through each row
    for row in csvreader:

        # Add values to list
        voter_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])

# Total votes should be equal to the number of voter IDs in the list
total_votes = len(voter_list)

# Count number of times each candidate appears in candidate list to get vote totals by candidate
khan_votes = candidate_list.count("Khan")
correy_votes = candidate_list.count("Correy")
li_votes = candidate_list.count("Li")
otooley_votes = candidate_list.count("O'Tooley")

# Create a dictionary of vote totals by candidate
vote_totals = {"Khan": khan_votes,
               "Correy": correy_votes,
               "Li": li_votes,
               "O'Tooley": otooley_votes}

# Winner is candidate with the greatest number of votes
winner = max(vote_totals, key=vote_totals.get)

# Calculate percentage of vote won by each candidate
khan_percent = "{:.3%}".format(khan_votes / total_votes)
correy_percent = "{:.3%}".format(correy_votes / total_votes)
li_percent = "{:.3%}".format(li_votes / total_votes)
otooley_percent = "{:.3%}".format(otooley_votes / total_votes)

# Create list for desired text output 
lines = []
lines.append(f"Election Results")
lines.append(f"-----------------------------")
lines.append(f"Total Votes: {total_votes}")
lines.append(f"-----------------------------")
lines.append(f"Khan: {khan_percent} ({khan_votes})")
lines.append(f"Correy: {correy_percent} ({correy_votes})")
lines.append(f"Li: {li_percent} ({li_votes})")
lines.append(f"O'Tooley: {otooley_percent} ({otooley_votes})")
lines.append(f"-----------------------------")
lines.append(f"Winner: {winner}")
lines.append(f"-----------------------------")

# Print output
for line in lines:
    print(line)

# Set path for output text file
output_file = os.path.join("analysis", "election_results.txt")

# Write items in list to text file, with each item on a new line
with open(output_file, "w") as textfile:
    textfile.writelines(line + "\n" for line in lines )
    textfile.close()