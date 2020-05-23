# Import modules
import os
import csv

#Read in file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Open file path
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip header row
    csv_header = next(csvreader)
    #Make empty lists to define variables
    financials = []
    months = []
    profit_change = []
   
#Create loop to return values to defined lists for each column
    for row in csvreader:
        months.append(row[0])
        financials.append(int(row[1]))

    #Calculate total number of months and net total of Profit/Losses
    total_months = len(months)
    net_total = sum(financials)
    
    #Return total number of months and net total of Profit/Losses to console
    print('Financial Analysis')
    print('---------------------------------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_total}')

    #Create loop to determine difference in Profit/Losses
    for f in range(0,total_months-1):
        profit_change.append(financials[f+1]-financials[f])
        
        #Return max, min and average of Profit/Losses
        max_change = max(profit_change)
        min_change = min(profit_change)
        avg_change = round(sum(profit_change)/(total_months-1),2)

        #Index month for max and min change
        max_date = months[profit_change.index(max_change)+1]
        min_date = months[profit_change.index(min_change)+1]
    
    #Return Profit/Loss statistics w/ dates to console
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {max_date} (${max_change})')
    print(f'Greatest Decrease in Profits: {min_date} (${min_change})')

#Export file results
output_path = os.path.join('analysis', 'analysis.txt')
with open(output_path, 'w') as txtwrite:
    print('Financial Analysis', file=txtwrite)
    print('---------------------------------------------------------', file=txtwrite)
    print(f'Total Months: {total_months}', file=txtwrite)
    print(f'Total: ${net_total}', file=txtwrite)
    print(f'Average Change: ${avg_change}', file=txtwrite)
    print(f'Greatest Increase in Profits: {max_date} (${max_change})', file=txtwrite)
    print(f'Greatest Decrease in Profits: {min_date} (${min_change})', file=txtwrite)