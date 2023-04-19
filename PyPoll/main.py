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

TEXT_PATH = os.path.join("PyPoll.txt")
# opens text file in order to write print statements to it
Text = open(TEXT_PATH, 'w')

os.chdir(os.path.dirname(os.path.realpath(__file__)))
# open csv file, read csv file, and  store header
with open(CSV_PATH, encoding='utf-8') as election_data_file:
    poll_reader = csv.reader(election_data_file)
    header = next(poll_reader)
    # for loop to find total votes and find and store votes per candidate in dictionary
    for row in poll_reader:
        total_votes += 1
        candidate_name = row[CANDIDATE_NAME_IDX]
        if candidate_name in votes_per_candidate:
            votes_per_candidate[candidate_name] += 1
        else:
            votes_per_candidate[candidate_name] = 1

# open and read csv file
with open(CSV_PATH, encoding='utf-8') as election_data_file:
    poll_reader = csv.reader(election_data_file)
    # multiple print statements to print both to console and text file
    print("Election Results", file=Text)
    print("Election Results")
    print("----------------------------", file=Text)
    print("----------------------------")
    print(f"Total Votes: {total_votes}", file=Text)
    print(f"Total Votes: {total_votes}")
    print("----------------------------", file=Text)
    print("----------------------------")
    # for loop to find percentages of votes per candidate
    for candidate in votes_per_candidate:
        percentages_per_candidate[candidate] = round(
            ((votes_per_candidate[candidate]/total_votes)*100), 3)
        output = (f"{candidate} {percentages_per_candidate[candidate]} % ({votes_per_candidate[candidate]})"
                  )  # formatted string as output variable
        print(output, file=Text)
        print(output)
        # max function to find winner
        winner_name = max(votes_per_candidate, key=votes_per_candidate.get)
print("-------------------------------", file=Text)
print("-------------------------------")
print(f"Winner: {winner_name}", file=Text)
print(f"Winner: {winner_name}")

Text.close()  # closes text file after all print statements
