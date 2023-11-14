import os
import csv

with open('PyPoll/Resources/election_data.csv') as file:
    csvreader = csv.reader(file, delimiter =',')

    # The total number of votes cast
    data_length = 0
    candidate_votes = {}
    #candidate_name.append([])
    unique_candidates = []
    winner = ''
    next(csvreader)
    for row in csvreader:
        #print(row)
        data_length = data_length + 1
        candidate_value = row[2]
        
        if candidate_value not in unique_candidates:
            unique_candidates.append(candidate_value)
            candidate_votes[candidate_value] = [0, 1]
        else:
            candidate_votes[candidate_value]=[0,candidate_votes.get(candidate_value)[1]+1]

    Winner = list(candidate_votes.keys())[0]
    print(Winner)
    for candidate in candidate_votes:
        #print(candidate)
        candidate_votes[candidate] = [round((candidate_votes.get(candidate)[1]/data_length)*100,3),candidate_votes.get(candidate)[1]]
        if(candidate_votes.get(candidate)[0] > candidate_votes.get(Winner)[0]):
            Winner = candidate
            #print(Winner)

    print('Election Results')
    print('-------------------------')
    print(f"Total Votes: {data_length}")
    print('-------------------------')
    for key, value in candidate_votes.items():
        print(key,': ',value[0],'% (',value[1],')', sep='')
              
        #print(candidate_votes.keys()
    print('-------------------------')
    print('Winner: ' + Winner)
    print('-------------------------')

    analysisOutput = open("PyPoll/Analysis/analysisOutput.txt", 'w')
    analysisOutput.write(f"Election Results\n-------------------------\nTotal Votes: {data_length}\n-------------------------\n")
    for key, value in candidate_votes.items():
        analysisOutput.write(f"{key}: {value[0]}% ({value[1]})\n")

    analysisOutput.write(f"-------------------------\nWinner: {Winner}\n-------------------------")
