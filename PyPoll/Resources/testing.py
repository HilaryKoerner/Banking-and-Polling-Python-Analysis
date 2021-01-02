#PyPoll homework

# import modules
import os
import csv

# Set path for file
poll_path = os.path.join('..', 'Resources', 'election_data.csv')

#open the csv file
with open(poll_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#skip the header
    next(csvreader,None)

#### MONTH COUNT & P&L TOTAL ######
#Month Count - bootcamp python day one lecture (lists)
##Profit Loss Total - commbination of month count code and https://www.geeksforgeeks.org/sum-function-python/
    votes = 0
    votes = []
    candidate_list = 0
    candidate_list = []
    khan = 'Khan'
    khan = []
    # kahn = 0
    correy = "Correy"
    correy = []
    # correy = 0
    li = "Li"
    li = []
    # li = 0
    otooley = "O'Tooley"
    otooley = []
    # otooley = 0
    for row in csvreader:
        votes_cast=str(row[0])
        votes.append(votes_cast)
        candidates=str(row[2])
        candidate_list.append(candidates)
        if candidate_list == khan:
            khan.append(candidate_list)
            
        elif candidate_list == correy:
            correy.append(candidate_list)
            
        elif candidate_list == li:
            li.append(candidate_list)

        elif candidate_list == otooley:
            otooley.append(candidate_list)
            
    total_votes = len(votes)
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(total_votes))
    print("----------------------------")
    kahn_votes = len(khan)
    print(kahn_votes)
    correy_votes = len(correy)
    print(correy_votes)
    li_votes = len(li)
    print(li_votes)
    otooley_votes = len(otooley)
    print(otooley_votes)
#-----------------------------------------------------------------#


    # #this doesnt print an error, but nothing happens
    # khan = 'Khan'
    # khan = []
    # correy = "Correy"
    # correy = []
    # li = "Li"
    # li = []
    # otooley = "O'Tooley"
    # otooley = []
    
    # if str(khan) in candidate_list:
    #     khan.append(candidate_list)
    #     kahn_votes = len(khan)
    #     print(kahn_votes)
    # if str(correy) in candidate_list:
    #     correy.append(candidate_list)
    #     correy_votes = len(correy)
    #     print(correy_votes)
    # if str(li) in candidate_list:
    #     li.append(candidate_list)
    #     li_votes = len(li)
    #     print(li_votes)
    # if str(otooley) in candidate_list:
    #     otooley.append(candidate_list)
    #     otooley_votes = len(otooley)
    #     print(otooley_votes)
    

    #-----------------------------------------------------#
    #this prints a long list of numbers. 
    # for name in candidate_list:
    #     if name == "Kahn":
    #         khan.append(name)
    #         kahn_votes = len(khan)
    #         print(kahn_votes)
    #     elif name == "Correy":
    #         correy.append(name)
    #         correy_votes = len(correy)
    #         print(correy_votes)
    #     elif name == "Li":
    #         li.append(name)
    #         li_votes = len(li)
    #         print(li_votes)
    #     else:
    #         otooley.append(name)
    #         otooley_votes = len(otooley)
    #         print(otooley_votes)
                


    

