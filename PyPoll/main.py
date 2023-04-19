# imports
import csv
import os
import sys


# constants
CSV_PATH = os.path.join("Resources", "election_data.csv")
CANDIDATE_NAME_IDX = 2
TEXT_PATH = os.path.join("PyPoll.txt")
# sys.stdout = open(TEXT_PATH, 'w')

Text = open(TEXT_PATH, 'w')

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

with open(CSV_PATH, encoding='utf-8') as election_data_file:  # opens file
    poll_reader = csv.reader(election_data_file)
    print("Election Results", file=Text)
    print("Election Results")
    print("----------------------------", file=Text)
    print("----------------------------")
    print(f"Total Votes: {total_votes}", file=Text)
    print(f"Total Votes: {total_votes}")
    print("----------------------------", file=Text)
    print("----------------------------")
    for item in votes_per_candidate:
        percentages_per_candidate[item] = round(
            ((votes_per_candidate[item]/total_votes)*100), 3)
        output = (f"{item} {percentages_per_candidate[item]} % ({votes_per_candidate[item]})"
                  )
        print(output, file=Text)
        print(output)
        winner_name = max(votes_per_candidate, key=votes_per_candidate.get)
print("-------------------------------", file=Text)
print("-------------------------------")
print(f"Winner: {winner_name}", file=Text)
print(f"Winner: {winner_name}")
Text.close()

# item = candidate in my dictionary
