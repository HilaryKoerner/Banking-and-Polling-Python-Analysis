# Modules
import os
import csv

# Set path for file
bank_file = os.path.join('..', 'Resources', 'budget_data.csv')

#open the csv file
with open(bank_file, 'r') as bank:
    csvreader = csv.reader(bank, delimiter=',')

    #skip the header
    next(csvreader,None)

    # #number of months (not working) - just prints each date
    # count = 0
    # for row in csvreader:
    #     month_year=str(row[0])
    #     count = month_year
    #     print(count)

    #number of months (not working) - counts each line as one, but doesnt sum
    # count = 0
    # for row in csvreader:
    #     month_year=str(row[0])
    #     count = month_year.count(month_year)
    #     print(count)

    #number of months (not working)
    # count = 0
    # for row in csvreader:
    #     for month_year in row:
    #         month_year=str(row[0])
    #         count = month_year.count(row[0])
    #         print(month_year)

    #create an empty list to hold results of looping
    # count = []
    # for row in csvreader:
    #     count.values(str(row[0]))
    # print(count)


    # #create an empty list to hold results of looping
    # letters = []
    # for letter in fish:
    #     letters.append(letter)
    # print(letters)
        

#-------------------------------------------------------------------------



    # # total of P&L (not working)
    # for row in csvreader:
    #     total = 0
    #     profit_loss=int(row[1])
    #     total = total + profit_loss
    #     print(total)

    #create an empty list to hold results of looping
    # total = 0
    # total = []
    # for row in csvreader:
    #     profit_loss=int(row[1])
    #     total.append(profit_loss)
    # print(total)
    
    #lists to store data
    # month_year = []
    # profit_loss= []
    # average_change = []
    # greates_increase = []
    # greates_decrease = []

    #create an empty list to hold results of looping
# letters = []
# for letter in fish:
#     letters.append(letter)
# print(letters)
