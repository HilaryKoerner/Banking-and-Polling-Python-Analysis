#This works - just need to turn numbers into percentages

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

#vote count - same as month count from PyBank (bootcamp python day one lecture (lists))
#put all votes in a list and all votes for each candidate in its own list
    votes = []
    can_khan = []
    can_correy = []
    can_li = []
    can_otooley = []
    for row in csvreader:
        votes_cast=str(row[0])
        votes.append(votes_cast)
        khan = "Khan"
        correy = "Correy"
        li = "Li"
        otooley = "O'Tooley"
        candidates = row[2]
        if candidates == khan:
            can_khan.append(candidates)
        if candidates == correy:
            can_correy.append(candidates)
        if candidates == li:
            can_li.append(candidates)
        if candidates == otooley:
            can_otooley.append(candidates)
    total_votes = len(votes)
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(total_votes))
    print("----------------------------")
    
    
    #find len of each vote for each candidate, find percentage, turn into percentage, print text
    #tutor helped me turn to percentage. it was an issue with *100 being outside parenthesis instead of inside
    khan_votes = len(can_khan)
    khan_percent = str(khan_votes/total_votes*100)
    float_kp = float(khan_percent)
    round_kp = round(float_kp,4)
    print("Khan: " + str(round_kp) + "% (" + str(khan_votes) + ")")
    
    correy_votes = len(can_correy)
    correy_percent = str(correy_votes/total_votes*100)
    float_cp = float(correy_percent)
    round_cp = round(float_cp,3)
    print("Correy: " + str(round_cp) + "% (" + str(correy_votes) + ")")
    
    li_votes = len(can_li)
    li_percent = str(li_votes/total_votes*100)
    float_lp = float(li_percent)
    round_lp = round(float_lp,3)
    print("Li: " + str(round_lp) + "% (" + str(li_votes) + ")")
    
    otooley_votes = len(can_otooley)
    otooley_percent = str(otooley_votes/total_votes*100)
    float_op = float(otooley_percent)
    round_op = round(float_op,3)
    print("O'Tooley: " + str(round_op) + "% (" + str(otooley_votes) + ")")
    
    print("-------------------------")
    
    ##conditionals to printer winner - candidate must have higher vote totals compared to all three candidates
    #similar to RPS activity
    if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > otooley_votes:
        print("Winner: Khan")
    if correy_votes > khan_votes and correy_votes > li_votes and correy_votes > otooley_votes:
        print("Winner: Correy")
    if li_votes > khan_votes and li_votes > correy_votes and li_votes > otooley_votes:
        print("Winner: Li")
    if otooley_votes > khan_votes and otooley_votes > correy_votes and otooley_votes > li_votes:
        print("Winner: O'Tooley")
    
    

