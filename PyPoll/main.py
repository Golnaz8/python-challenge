# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates_list = []
candidate_votes = {}


# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1


        # Get the candidate's name from the row
        candidate_name = row[2]


        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates_list:
            candidates_list.append(candidate_name)
            candidate_votes[candidate_name] = 0


        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

    

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"\nTotal vote count = {total_votes}")


    # Write the total vote count to the text file
    result = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    txt_file.write(result)



    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidates_list:


        # Get the vote count and calculate the percentage
        vote_count = candidate_votes[candidate]
        vote_persentage = (vote_count / total_votes) * 100

        round_vote_percentage = round(vote_persentage , 3)


        # Update the winning candidate if this one has more votes
        if vote_count > winning_count : 
            winning_count = vote_count
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        candidate_output = f"{candidate} : {vote_count} vote count and {round_vote_percentage}% percent vote"
        print(candidate_output)
        candidate_output_txt = (
            f"{candidate}: {round_vote_percentage}% ({vote_count})\n"
        )
        txt_file.write(candidate_output_txt)



    # Generate and print the winning candidate summary
    winning_percentage = round((winning_count / total_votes) * 100, 3)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)



    # Save the winning candidate summary to the text file
    winning_candidate_summary_txt = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    txt_file.write(winning_candidate_summary_txt)
