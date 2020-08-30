# PyBank Challenge
# -------------------------------------------------------

# Import modules
import os
import csv
import statistics

# Set path
csvpath = os.path.join("resources","budget_data.csv")

# Create list to store months + month-over-month changes
months = []
delta_list = []

# Create variable to store profit/loss
pnl_total = 0
pnl_month = 0

# Read th3 csv file
with open(csvpath) as csvfile:
    
    # create object to read csvfile
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row
    header = next(csvreader)

    # Loop through each row 
    for row in csvreader:

        # Add month to list
        months.append(row[0])

        # Add profit/loss to total
        pnl_total += float(row[1])

        # Calculate current month delta and add to list
        delta = float(row[1]) - pnl_month
        delta_list.append(delta)

        # Reset profit/loss for month
        pnl_month = float(row[1])


# Calculate number of months
num_months = len(months)

# Remove first delta from list and calcualte average change
delta_list.pop(0)
avg_change = round(statistics.mean(delta_list), 2)

# Check that dataset contains a positive change in profits
# Calculate greatest increase in profits
if max(delta_list) > 0:
    max_increase = max(delta_list)
else:
    print("There are no increases in profits in the dataset")

# Determine index of max increase and month of max increase
# To get month, must add 1 to index since we removed the first element of delta_list
max_increase_index = int(delta_list.index(max_increase))
max_increase_month = months[max_increase_index + 1]

# Check that dataset contains a negative change in profits
# Calculate greatest decrease in profits
if min(delta_list) < 0:
    max_decrease = min(delta_list)
else:
    print("There are no decreases in profits in the dataset")

# Determine index of max increase and month of max increase
# To get month, must add 1 to index since we removed the first element of delta_list
max_decrease_index = int(delta_list.index(max_decrease))
max_decrease_month = months[max_decrease_index + 1]

# Create list for desired text output
lines = []
lines.append("Financial Analysis")
lines.append("-------------------------------")
lines.append(f"Total Months: ${num_months}")
lines.append(f"Total: ${pnl_total}")
lines.append(f"Average Change: ${avg_change}")
lines.append(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
lines.append(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")

# Print output
for line in lines:
    print(line)

# Set path for output text file
output_file = os.path.join("analysis", "budget_analysis.txt")

# Write items in list to text file, with each item on a new line
with open(output_file, "w") as textfile:
    textfile.writelines(line + "\n" for line in lines )
    textfile.close()