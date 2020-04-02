import csv

# Load files
file_load = "/Users/petr/Desktop/Data_School/python/python-challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv"
file_analysis = "/Users/petr/Desktop/Data_School/python/python-challenge/PyBank/Analysis/budget_analysis.rtf"

# Set Variables
total_months = 0
total_proift_loss = 0

prev_profit_loss = 0
profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]

profit_loss_change = []

# read file    
with open(file_load,'r') as csvfile: 
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)
    
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

        # Identify the greatest increase
        if (profit_loss_change > greatest_increase[1]):
            greatest_increase[1] = profit_loss_change
            greatest_increase[0] = row["Date"]

        if (profit_loss_change < greatest_decrease[1]):
            greatest_decrease[1] = profit_loss_change
            greatest_decrease[0] = row["Date"]

        # Add to the profit_loss_change list
        profit_loss_change.append(int(row["Profit/Losses"]))
        
    # Set Profit/Losses Average
    profit_loss_avg = sum(profit_loss_change) / len(profit_loss_change)

# Show Results
print()
print()
print()
print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + "$" + str(total_revenue))
print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")