# Modules
import os
import csv

# Set path for file
bank_file = os.path.join('..', 'Resources', 'budget_data.csv')

#lists to store data
month_year = []
profit_loss= []
# average_change = []
# greates_increase = []
# greates_decrease = []

#open the csv file
with open(bank_file, 'r') as bank:
    csvreader = csv.reader(bank, delimiter=',')

    #skip the header
    next(csvreader,None)
    
    #loop through each row of data and print just the year and P&L
    #float allows you to analyze numbers with decimals (not actually sure why this is needed)
    for row in csvreader:
        month_year.count(row[0])

        #loop through each row of data and print just the year and P&L
    #float allows you to analyze numbers with decimals (not actually sure why this is needed)
    for row in csvreader:
        month_year=row[0]
        profit_loss=row[1]
        if profit_loss >= str(0):
            print(month_year,profit_loss)