import csv
csvpath = 'Resources/election_data.csv'
with open(csvpath, encoding='utf') as File:
    reader = csv.reader(File, delimiter=',')
    next(reader, None)
    Votes = 0
    CanDict = {}
    for row in reader:
        Votes += 1
        CurrentCandidate = row[2]
        if CurrentCandidate not in CanDict:
            CanDict[CurrentCandidate] = [1, 0]
        else:
            CanDict[CurrentCandidate][0] += 1
    for Candidate in CanDict:
        CanDict[Candidate][1] = CanDict[Candidate][0]/Votes*100
    print(CanDict)

# CandidatePercentage = (CanDict[CurrentCandidate][0]/Votes)*100
# print(CandidatePercentage)
# print(CanDict)
# print(Votes)
# import csv
# csvpath = "Resources/election_data.csv"
# with open(csvpath, 'r') as Election_Data_File:
#     PollRecords = csv.reader(Election_Data_File, delimiter=",")
#     PollRecords = next(PollRecords)
#     CandidateDict = {}
#     Votes = 0
#     for row in PollRecords:
#         Votes += 1
#         CurrentCandidate = row[2]
#         if CurrentCandidate not in CandidateDict:
#             CandidateDict["Current_Candidate"] = [1]
#         else:
#             CandidateDict[CurrentCandidate][0] += 1
# print(row)
# print(Votes)
