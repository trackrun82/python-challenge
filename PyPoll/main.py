# Import modules
import os
import csv

#Read in file
csvpath = os.path.join('Resources', 'election_data.csv')

#Open file path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip header row
    csv_header = next(csvreader)
    #Make empty list to define variable
    candidates = []
   
#Create loop to return values to defined list for candidate column
    for row in csvreader:
        candidates.append((row[2]))

    #Calculate total number of rows(votes)
    total_rows = len(candidates)
 
#Return total number of rows(votes) to console
    print('Election Results')
    print('---------------------------------------------------------')
    print(f'Total Votes: {total_rows}')
    print('---------------------------------------------------------')

    #Create empty dictionary to store unique candidates and their vote counts
    unique_candidates = {}
    #Create loop that counts each time a unique candidate is found in candidate list 
    for name in candidates:
        if name not in unique_candidates:
            unique_candidates[name]=1
        else:
            unique_candidates[name]+=1

    #Create a loop to return each key:value in unique_candidates dictionary along w/ percent on separate line
    for key, value in unique_candidates.items():
        print(key,":",round(value/total_rows*100,3),"% (",value,")")
    
    #Define the winner by referencing the key of the max value from the unique_candidates dictionary and print to console
    print('---------------------------------------------------------')
    Winner = max(unique_candidates,key=unique_candidates.get)
    print(f'Winner: {Winner}')
    print('---------------------------------------------------------')

#Export file results
output_path = os.path.join('analysis', 'analysis.txt')
with open(output_path, 'w') as txtwrite:
    print('Election Results', file=txtwrite)
    print('---------------------------------------------------------', file=txtwrite)
    print(f'Total Votes: {total_rows}', file=txtwrite)
    print('---------------------------------------------------------', file=txtwrite)
    for key, value in unique_candidates.items():
        print(key,":",round(value/total_rows*100,3),"% (",value,")", file=txtwrite)
    print('---------------------------------------------------------', file=txtwrite)
    print(f'Winner: {Winner}', file=txtwrite)
    print('---------------------------------------------------------', file=txtwrite)
  