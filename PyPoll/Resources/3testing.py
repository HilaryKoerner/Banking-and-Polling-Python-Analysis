#PyPoll homework

# import modules
import os
import csv

# Set path for file
poll_path = os.path.join('..', 'Resources', 'election_data.csv')

#VOTE COUNT: open the csv file
with open(poll_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#VOTE COUNT: skip the header
    next(csvreader,None)

#### VOTE COUNT ######
#vote count - same as month count from PyBank (bootcamp python day one lecture (lists))
    votes = []
    khan = []
    # correy = []
    # li = []
    # otooley = []
    for row in csvreader:
        votes_cast=str(row[0])
        votes.append(votes_cast)
        candidates = str(row[2])
        khan = "Khan"
        # correy = "Correy"
        # li = "Li"
        # otooley = "O'Tolley"
        if candidates == khan:
            khan.append(candidates)
        # if candidates == correy:
        #     correy.append(candidates)
        # if candidates == li:    
        #     li.append(candidates)
        # if candidates == otooley:
        #     otooley.append(candidates)
    total_votes = len(votes)
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(total_votes))
    print("----------------------------")
    khan_votes = len(khan)
    print("Khan: " + str(khan_votes))
    # correy_votes = len(correy)
    # print("Correy: " + str(correy_votes))
    # li_votes = len(li)
    # print("Li: " + str(li_votes))
    # otooley_votes = len(otooley)
    # print("O'Tooley: " + str(otooley_votes))
#------------------------------------------------------------------------------------------S
