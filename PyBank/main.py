# help on coding with indentation, the for loop and formatting from TA Sunshine via AskBCS
# imports
import csv

# defining variables
csvpath = "Resources/budget_data.csv"
total_months = 0
net_total = 0
change = 0
max_change = 0
min_change = -1
average_change = 0
change_total = 0

with open(csvpath, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # storing header
    previous_total = 0  # setting variable
    for row in csv_reader:
        # calculating total months by counting every row looped through to get to total
        total_months += 1
        # calculating net total by adding every value in profit/loss column to the one before it
        net_total = net_total + int(row[1])
        # setting current total as the value in the current row profit/loss column
        current_total = int(row[1])
        # calculating the change in profit/loss between previous row and current row
        if previous_total == 0:
            previous_total = current_total
        else:
            change = current_total - previous_total
            change_total += change
            # previous_change = current_total - previous_total
            # resetting previous_total as current profit/loss value for the loop
            previous_total = int(row[1])
            if change > max_change:  # finding max change and date
                max_change = change
                max_date = row[0]
            elif change < min_change:  # finding min change and date
                min_change = change
                min_date = row[0]
average_change = round(change_total/(total_months - 1), 2)

# exports
output = (
    f"Financial Analysis\n"
    f"--------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {max_date} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_date} (${min_change})\n"
)
print(output)

with open('PyBank.txt', 'w') as f:
    f.write(output)
