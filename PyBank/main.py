# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)


    # Track the total and net change
    total_months += 1
    total_net += int(first_row[1])


    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        

        # Track the net change
        total_net += int(first_row[1])


        # Calculate the greatest increase in profits (month and amount)


        # Calculate the greatest decrease in losses (month and amount)



# Calculate the average net change across the months


# Generate the output summary


# Print the output


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
