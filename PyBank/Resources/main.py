#PyBank homework

# import modules
import os
import csv

# Set path for file
bank_path = os.path.join('..', 'Resources', 'budget_data.csv')

#open the csv file
with open(bank_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#skip the header
    next(csvreader,None)

#### MONTH COUNT & P&L TOTAL ######
    date = 0
    date = []
    total = 0
    total = []
    for row in csvreader:
        month_year=str(row[0])
        date.append(month_year)
        profit_loss=int(row[1])
        total.append(profit_loss)
    print(len(date))
    sum = sum(total)
    print(sum)

