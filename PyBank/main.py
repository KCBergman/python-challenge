# imports
import csv


# variables
csvpath = "Resources/budget_data.csv"
total_months = 0
net_total = 0
change = 0
max_change = 0
min_change = -1
average_change = 0
change_total = 0

# open csv_file and store header
with open(csvpath, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # storing header
    previous_total = 0
    # for loop to find total months, net total, maximum increase, and maximum decrease in profits
    for row in csv_reader:
        total_months += 1
        net_total = net_total + int(row[1])
        current_total = int(row[1])
        if previous_total == 0:
            # set previous total to current total for the first row
            previous_total = current_total
        else:
            change = current_total - previous_total
            change_total += change
            # set the previous total to current total for all subsequent rows
            previous_total = int(row[1])
            if change > max_change:
                max_change = change
                max_date = row[0]
            elif change < min_change:
                min_change = change
                min_date = row[0]

# finding average change in profits/losses for the entire period
# need to minus 1 from total months because there will be one less change than items
average_change = round(change_total/(total_months - 1), 2)

# output statement
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
# write output statement to text file
with open('PyBank.txt', 'w') as f:
    f.write(output)
