#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

import csv
import os

path = './Resources/election_data.csv'

total_votes=0
cand_list= []
cand_votes= []

#Calc total number of votes & get list of candidates
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)
    index = 0
    #Count
    for row in csv_reader:
        #Count of rows/votes
        total_votes=total_votes+1
        #Append all candidates to a list
        cand_list.append(row[2])
    #Remove duplicates from Candidates List
    cand_list=list(dict.fromkeys(cand_list))
    #Add unique candidates to a dictionary
    for ea in cand_list:
        cand = {"Name": ea,"Votes": 0}
        cand_votes.append(cand)

#Loop back through to calc total votes per candidate
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)
    #Loop back through rows
    for row in csv_reader:
        for ea in cand_votes:
            #Add vote to dictionary if row is candidate name
            if (row[2]==ea["Name"]):
                ea["Votes"]=ea["Votes"]+1

#Find Most Votes
most_votes = 0
for ea in cand_votes:
    if (ea["Votes"]>most_votes):
        most_votes = ea["Votes"]
        winner = ea["Name"]

 
print('Election Results\n------------------\nTotal Votes: '+str(total_votes)+'\n------------------')
for ea in cand_votes:
    print(ea["Name"]+": "+str(round(ea["Votes"]*100/total_votes,3))+"% ("+str(ea["Votes"])+")")
print('------------------\nWinner: '+winner+' \n------------------')


text_context = ['Election Results\n------------------\nTotal Votes: '+str(total_votes)+'\n------------------']

with open('./Analysis/PyPoll Analysis.txt', 'w') as txt_file:
    txt_file.writelines(text_context)
    for ea in cand_votes:
        txt_file.writelines(ea["Name"]+": "+str(round(ea["Votes"]*100/total_votes,3))+"% ("+str(ea["Votes"])+")\n")
    txt_file.writelines('------------------\nWinner: '+winner+' \n------------------')


# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.