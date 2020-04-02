import csv

file_load = "/Users/petr/Desktop/Data_School/python/python-challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv"
#file_analysis = "/Users/petr/Desktop/Data_School/python/python-challenge/PyBank/Analysis/Profit_Analysis.docx"

# Set Variables
total_months = 0
total_proift_loss = 0

prev_profit_loss = 0
profit_loss_change = 0
profit_increase = ["", 0]
profit_decrease = ["", 9999999]

profit_loss_change = []

# read file    
with open(file,'r') as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=",")

# Loop through all the rows of data collected
for row in csvreader:

        # Calculate the totals
        total_months = total_months + 1
        total_proift_loss = total_proift_loss + int(row["Profit/Losses"])
        print(row)

        # Keep track of changes
        profit_loss_change = int(row["Profit/Losses"]) - prev_profit_loss
        print(profit_loss_change)

        # Reset Profit/Losses value
        prev_profit_loss = int(row["Profit/Losses"])
        print(row)

        # Identify change
        if (profit_loss_change > profit_increase[1]):
            profit_increase[1] = profit_loss_change
            profit_increase[0] = row["Date"]