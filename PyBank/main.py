# finding total months
import csv
csvpath = "Resources/budget_data.csv"
with open(csvpath, encoding='utf') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)
    Total_Months = len(list(csv_reader))
    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {Total_Months}")

    csv_file.seek(0)
    next(csv_reader, None)
    NetTotal = 0
    rows = []
    for row in csv_reader:
        NetTotal = NetTotal + int(row[1])
        rows.append(int(row[1]))
    ProfitLoss = [rows[i + 1] - rows[i] for i in range(len(rows)-1)]
    ProfitLossTotal = sum(ProfitLoss)
    ProfitLossAverage = ProfitLossTotal/85
    print(f"Average Change: ${ProfitLossAverage:.2f}")
    print(f"Total: ${NetTotal}")

with open(csvpath, encoding='utf') as csv_file:
    # opening file and allowing python to access and work the csv file; and we want to keep working on it so saving as a variable
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader, None)
    rows = []
    for row in csv_reader:
        rows.append(int(row[1]))
    Change = [rows[i + 1] - rows[i] for i in range(len(rows)-1)]
    Max = max(Change)
    Min = min(Change)
    print(f"Greatest Increase in Profits: ${Max}")
    print(f"Greatest Decrease in Profits: ${Min}")
