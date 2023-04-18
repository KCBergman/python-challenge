# finding total months
import csv
csvpath = "Resources/budget_data.csv"
total_months = 0
total_months_less1 = 0
net_total = 0
rows = []
date = []
profit_loss = 0
profit_loss_total = 0
profit_loss_average = 0
change = []

with open(csvpath, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for row in csv_reader:
        total_months += 1
        net_total = net_total + int(row[1])
        rows.append(int(row[1]))
        date.append(row[0])
        profit_loss = rows[i+1]-rows[i]
        print(profit_loss)
        for i in range(len(rows)-1):
            change.append(profit_loss[i] - profit_loss[i-1])
            AverageChange = sum(change)/len(change)
            max_change = max(change)
            min_change = min(change)
            MaxDate = str(date[change.index(max(change))])
            MinDate = str(date[change.index(min(change))])

            # change = rows[i+1] - rows[i]
            # if change > max:
            #     max = change
            # elif change < min:
            #     min = change
            # could just do date for max by looking at date =row[2]??
        profit_loss_total = sum(profit_loss)

        # figure out how to do this and have it be total months -1 without getting divide by zero
    total_months_less1 = total_months - 1
    profit_loss_average = profit_loss_total/total_months_less1
    output_string = f"Financial Analysis\n ---------------------------\n Total Months: {total_months}\n Average Change: {profit_loss_average}\n Total: ${net_total}\n Greatest Increase in Profits: ${max}\n Greatest Decrease in Profits: ${min} \n"
    print(output_string)

    # (
    #     f"Financial Analysis\n"
    #     "--------------------------------\n"
    #     "Total Months: {total_months}\n"
    #     "Average Change: {profit_loss_average:.2f}\n"
    #     "Total: ${net_total}\n"
    #     "Greatest Increase in Profits: ${max}\n"
    #     "Greatest Decrease in Profits: ${min}\n"
    # )
print(output_string)

#     print("Financial Analysis")
#     print("------------------------------")
#     print(f"Total Months: {Total_Months}")
#     print(f"Average Change: ${ProfitLossAverage:.2f}")
#     print(f"Total: ${NetTotal}")
#     print(f"Greatest Increase in Profits: ${Max}")
#     print(f"Greatest Decrease in Profits: ${Min}")

#     for row in csv_reader:
#         NetTotal = NetTotal + int(row[1])
#         rows.append(int(row[1]))
#     ProfitLoss = [rows[i + 1] - rows[i] for i in range(len(rows)-1)]
#     ProfitLossTotal = sum(ProfitLoss)
#     ProfitLossAverage = ProfitLossTotal/85


# with open(csvpath, encoding='utf') as csv_file:
#     # opening file and allowing python to access and work the csv file; and we want to keep working on it so saving as a variable
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     next(csv_reader, None)
#     rows = []
#     for row in csv_reader:
#         rows.append(int(row[1]))
#     Change = [rows[i + 1] - rows[i] for i in range(len(rows)-1)]
#     Max = max(Change)
#     Min = min(Change)
