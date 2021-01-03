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
#Month Count - bootcamp python day one lecture (lists)
##Profit Loss Total - commbination of month count code and https://www.geeksforgeeks.org/sum-function-python/
    date = 0
    date = []
    total = []
    for row in csvreader:
        month_year=str(row[0])
        date.append(month_year)
        profit_loss=int(row[1])
        total.append(profit_loss)
    sum_total = sum(total, 0)
    month_count = len(date)
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(month_count))
    print("Total: $" + str(sum_total))

#open the csv file
with open(bank_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#skip the header
    next(csvreader,None)
    #iterate through the 
    difference = {}
    prevrow = next(csvreader)
    prevdate = prevrow[0]
    prevpl = int(prevrow[1])

    for row in csvreader:
        difference[row[0]] = int(row[1])-prevpl
        prevdate = row[0]
        prevpl = int(row[1])

    #this pulls out the key that is paired with the max/min value
    # https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
    keymax = max(difference, key= lambda x: difference[x])
    keymin = min(difference, key= lambda x: difference[x]) 
    
    # pull out just values from dictionary to find min and max https://www.geeksforgeeks.org/python-dictionary-values/
    # https://careerkarma.com/blog/python-typeerror-int-object-is-not-callable/ (used to debug "sum in not callable")
    pllist = difference.values()
    ROC = str(sum(pllist)/month_count)
    round_ROC = round(int(ROC))
    print("Average Change: $" + round_ROC)
    increase = (max(pllist))
    print("Greatest Increase in Profits: " + keymax + " $" + str(increase))
    decrease = (min(pllist))
    print("Greatest Decrease in Profits: " + keymin + " $" + str(decrease))
    

