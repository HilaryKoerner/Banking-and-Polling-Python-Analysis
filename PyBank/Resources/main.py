#PyBank homework

# import modules
import os
import csv

# Set path for file
bank_path = os.path.join('PyBank', 'Resouces', 'budget_data.csv')

#open the csv file
with open(bank_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# # Define the function and have it accept the 'bank_data' as its sole parameter
# def bank(bank_data):
#     # For readability, it can help to assign your values to variables with descriptive names
#     month_year = str(bank_data[0])
#     profit_loss = int(bank_data[1])

#     #total number of months
#     total_months = len(month_year)

#     #total (add P&Ls together)
#     total = sum(profit_loss)

#     print(bank)
    

