import csv
file = "/Users/petr/Desktop/Data_School/python/python-challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv"
with open(file,'r') as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=",")

# Set Variables
total_months = 0
total_proift/loss = 0

prev_profit/loss = 0
profit/loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]

profit/loss_change = []

    # Lopp through all the rows of data collected
    for row in reader:

        #Calculate the totals
        total_months = total_months + 1
        total_proift/loss = total_proift/loss + int(row["Profit/Losses"])
        #print(row)

        # Keep track of changes
        profit/loss_change = int(row["Profit/Losses"]) - prev_profit/loss
        # print(profit/loss_change)