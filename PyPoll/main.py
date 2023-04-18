# imports
import csv
import os


# constants
CSV_PATH = os.path.join("Resources", "election_data.csv")
CANDIDATE_NAME_IDX = 2

# variables
total_votes = 0
votes_per_candidate = {}
percentages_per_candidate = {}

# inputs
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH, encoding='utf-8') as election_data_file:  # opens file
    poll_reader = csv.reader(election_data_file)  # reads files
    header = next(poll_reader)  # stores file
    # for loop
    for row in poll_reader:
        total_votes += 1
        candidate_name = row[CANDIDATE_NAME_IDX]
        if candidate_name in votes_per_candidate:
            votes_per_candidate[candidate_name] += 1
        else:
            votes_per_candidate[candidate_name] = 1
for item in votes_per_candidate:
    percentages_per_candidate[item] = round(
        (votes_per_candidate[item]/total_votes)*100)
    # for item in votes_per_candidate:
    candidate_percentage = f"{candidate_name} {percentages_per_candidate[item]}"
    print(candidate_percentage)

    # print(votes_per_candidate)
    # print(percentages_per_candidate)
    # output = (
    #     "Election Results\n"
    #     "------------------------------\n"
    #     f"Total Votes: {total_votes} \n"
    #     "------------------------------\n"
    #     f'{votes_per_candidate}: {candidate_percentage}\n'
    # )
    # print(output)
    # election_data_file.seek(0)

# print("Election Results")
# print("--------------------------------")
# print(f"Total Votes: {total_votes}")
# print("---------------------------------")

# needed this url to figure out this code https://stackoverflow.com/questions/37438550/how-can-i-count-occurrences-of-values-in-a-list-of-dicts
# Ask the Class Slack and study group and tutor and talking to Aaron, Kirsten, Aaron O., and Joanna from class also helped with figuring out needing to use dictionaries
# Joanna pointed me towards the Collections import for python and the counter function
