import pandas as pd
import csv
from pathlib import Path

print(f"Current Working Directory:{Path.cwd()}")

csvpath = Path('/Users/jiwookkim/Desktop/python-homework/PyBank/budget_data.csv')

#Instantiaing variables
months = 0
npl = 0
monthly_change = 0
next_value = 0
dates = []
profits = []

#instantiate for best and worst performance
best_increase = 0
worst_decrease= 0

#open the csv file as an object
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    #read the header
    header = next(csvreader)
    
    #get previous values for calculating the changes
    previous_value = next(csvreader)
    npl += int(previous_value[1])
    months += 1
    
    #Read each row of data after the header
    for row in csvreader:
        
        #into empty dates list, append date from csv Date column
        dates.append(row[0])
        months += 1
        
        #month to month change average
        #calculating change
        monthly_change = int(row[1]) - int(previous_value[1])
        profits.append(monthly_change)
        average_monthly_change = round(sum(profits) / months, 2)
        
        #update previous_value
        previous_value = row

        
        #calculating total profit/losses
        npl = npl + int(row[1])
        
        #monthly_change comparison
        if monthly_change >= best_increase:
            best_increase = monthly_change
            best_increase_month = row[0]
        elif monthly_change <= worst_decrease:
            worst_decrease = monthly_change
            worst_decrease_month = row[0]
        
        


        
        
print(f"Financial Analysis")
print(f"-----------------------------------")
print(f"Total Months: {months}")
print(f"Total : {npl}")
print(f"Average Change : ${average_monthly_change}")
print(f"Greatest Increase in Profits: {best_increase_month} (${best_increase})")
print(f"Worst Decrease in Profits {worst_decrease_month} (${worst_decrease})")


#Set the path for the output.csv
output_path = Path('/Users/jiwookkim/Desktop/python-homework/PyBank/output.txt')

#open the output path as a file 
with open(output_path, 'w', newline='') as file:
    file.write(f"Financial Analysis:\n")
    file.write(f"-----------------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total : {npl} USD\n")
    file.write(f"Average Change : ${average_monthly_change} USD\n")
    file.write(f"Greatest Increase in Profits: {best_increase_month} (${best_increase}) USD\n")
    file.write(f"Worst Decrease in Profits {worst_decrease_month} (${worst_decrease}) USD")
                                                                             
    file.close()

