import os
import csv

with open('PyBank/Resources/budget_data.csv') as file:
    csvreader = csv.reader(file, delimiter=',')

    # Read through each row of data under the header
    data_length = 0
    profit_losses = 0
    average_change = []
    previous_row = 0
    greatestInc = ["", 0]
    greatestDecs = ["", 9999999999]
    next(csvreader)
    for row in csvreader:
        data_length = data_length + 1
        # profit_losses = profit_losses + int(row[1])
        profit_losses += int(row[1])
        average_change.append(int(row[1]) - previous_row)
        if(int(greatestInc[1]) < average_change[-1]):
            greatestInc[0] = row[0]
            greatestInc[1] = average_change[-1]
        if(int(greatestDecs[1]) > average_change[-1]):
            greatestDecs[0] = row [0]
            greatestDecs[1] = average_change[-1]
        previous_row = int(row[1])
    average_change.pop(0)
    #print(sum(average_change))
    average_change = sum(average_change)/len(average_change)

    print("Finacial Analysis")
    print("----------------------------")
    print("Total Months:", data_length)  
    print(f"Total: ${profit_losses}")
    print(f"Average Change: ${round(average_change,2)}")
    print(f"Greatest Increase in Profits: {greatestInc[0]} (${greatestInc[1]})")
    print(f"Greatest Decrease in Profits: {greatestDecs[0]} (${greatestDecs[1]})")

    analysisOutput = open("PyBank/Analysis/analysisOutput.txt", 'w')
    analysisOutput.write(f"Finacial Analysis\n----------------------------\nTotal Months: ${data_length}\nTotal: ${profit_losses}\nAverage Change: ${round(average_change,2)}\nGreatest Increase in Profits: {greatestInc[0]} (${greatestInc[1]})\nGreatest Decrease in Profits: {greatestDecs[0]} (${greatestDecs[1]})")

