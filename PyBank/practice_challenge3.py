import csv

# Files to load (Remember to change these)
csvpath = "Resources/budget_data.csv"


# Read the csv and convert it into a list of dictionaries
with open(csvpath, encoding='utf') as budget_data:
    reader = csv.reader(budget_data, delimiter=',')

    # use of next to skip first title row in csv file
    next(reader)
    Profit_Loss = []
    Date = []
    Profit_Loss_Change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0
    for row in reader:

        Profit_Loss.append(int(row[1]))
        Date.append(row[0])
    TotalMonths = len(Date)
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(Date))
    print("Total Revenue: $", sum(Profit_Loss))

    # in this loop I did total of difference between all row of column "Profit_Loss_Change" and found total revnue change. Also found out max revenue change and min revenue change.
    for i in range(1, len(Profit_Loss)):
        Profit_Loss_Change.append(Profit_Loss[i] - Profit_Loss[i-1])
        AverageChange = sum(Profit_Loss_Change)/len(Profit_Loss_Change)

        Max = max(Profit_Loss_Change)

        Min = min(Profit_Loss_Change)

        MaxDate = str(Date[Profit_Loss_Change.index(max(Profit_Loss_Change))])
        MinDate = str(Date[Profit_Loss_Change.index(min(Profit_Loss_Change))])

    print(f"Average Change: {AverageChange:.2f}")
    print(f"Greatest Increase in Revenue: {MaxDate} $({Max})")
    print(f"Greatest Decrease in Revenue: {MinDate} $({Min})")

# https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in I used this stack overflow to figure out how to get the greatest increase and greatest decrease months to print out
# finding average change per month
# import csv
# csvpath = "Resources/budget_data.csv"
# with open(csvpath, encoding='utf') as csv_file:
#     # opening file and allowing python to access and work the csv file; and we want to keep working on it so saving as a variable
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     next(csv_reader, None)
#     Change = 0
#     for row in csv_reader:
#         if int(row[1]) > Change:
#             GreatestChange = int(row[1])
#     print(GreatestChange)

# csvpath = "Resources/budget_data.csv"
# with open(csvpath, encoding='utf') as csv_file:
#     # opening file and allowing python to access and work the csv file; and we want to keep working on it so saving as a variable
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     csv_reader = next(csv_reader, None)
#     for csv_reader in csv_reader
#     Change = [[csv_reader[i + 1] - csv_reader[i]
#                for i in range(len(csv_reader)-1)]]
#     Date = []
#     for row in csv_reader:
#         if row[0] not in Date:
#             Date.append(row[0])
#         if row[1] not in Change:
#             Change.append(row[1])
# print(Date, Change)
