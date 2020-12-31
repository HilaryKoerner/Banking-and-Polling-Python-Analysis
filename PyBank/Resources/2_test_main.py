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

    # #count number of months (This works, kinda!!!!)
    # #https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python
    # lines = len(list(csvreader))
    # print(lines)
    
    # # total of P&L (not working - just prints each total into one list)
    # month_year = 0
    # month_year = []
    # for row in csvreader:
    #     month_year=str(row[0])
    #     month_year.append(month_year)
    # print(month_year)

    # #number of months (not working) - just prints each date
    # count = 0
    # for row in csvreader:
    #     month_year=str(row[0])
    #     count = month_year
    #     print(count)

    # #number of months (not working) - counts each line as one, but doesnt sum
    # count = 0
    # for row in csvreader:
    #     month_year=str(row[0])
    #     count = month_year.count(month_year)
    #     print(count)

    # #number of months (not working)
    # count = 0
    # for row in csvreader:
    #     for month_year in row:
    #         month_year=str(row[0])
    #         count = month_year.count(row[0])
    #         print(month_year)

    # #create an empty list to hold results of looping
    # count = []
    # for row in csvreader:
    #     count.values(str(row[0]))
    # print(count)
  
#---------------------------------------------------------------------------------------------------------------------------------------------------

# # total of P&L (not working - just prints each total, not the sum)
#     for row in csvreader:
#         total = 0
#         profit_loss=int(row[1])
#         total = total + profit_loss
#         print(total)

##total of P&L (not working - just prints each total into one list)
    total = 0
    total = []
    for row in csvreader:
        profit_loss=int(row[1])
        total.append(profit_loss)
    print(total)

# # total of P&L (not working - does not sum the total)
#     total = 0
#     total = []
#     for row in csvreader:
#         profit_loss=int(row[1])
#         total.append(profit_loss)
#     print(sum(total)

    #sum all totals (this does not work - no error, but nothing happens)
    #https://stackoverflow.com/questions/51325127/using-returned-outputs-from-one-function-in-another-in-python
    # def bankdata():
    #     totals=[]
    #     for i in row(1):
    #         totals.append(totals)
    #     return totals
    #     print(totals)
    
    # #sum all totals (this does not work - unsupported operand)
    # for row in csvreader:
    #     for i in row[1]:
    #         total = 0
    #         total = int(total + i)
    #         print(total)

    # #sum all totals with a function (this does nothing - no error)
    # for row in csvreader:
    #     def sum_totals(sum(total)):
    #         print("Profit Loss Total: ", total)
    #     total = row[1]

    # #get rate of change

    # #get biggest increase

    # #get biggest decrease