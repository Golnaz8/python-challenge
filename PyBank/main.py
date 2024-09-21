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
greatest_increase = ["Jan", 0]
greatest_decrease = ["Jan", 0]

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
    pre_month_net = int(first_row[1])


    # Process each row of data
    for row in reader:

        # Track the total month and total net
        total_months += 1
        total_net += int(row[1])
        

        # Track the net change
        net_change = int(row[1]) - pre_month_net
        pre_month_net = int(row[1])
        net_change_list.append(net_change)
        


        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase[0] = str(row[0])
            greatest_increase[1] = net_change




        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change



# Calculate the average net change across the months
average_net_change = sum(net_change_list) / len(net_change_list)


# Generate the output summary
rounded_change = round(average_net_change, 2)

date_inc = []
date_format = greatest_increase[0]
date_inc = date_format.split("-")

date_dec = []
date_format = greatest_decrease[0]
date_dec = date_format.split("-")

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${rounded_change}\n"
    f"Greatest Increase in Profits: {date_inc[1]}-{date_inc[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {date_dec[1]}-{date_dec[0]} (${greatest_decrease[1]})\n"
)


# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
