import csv

# Load files
file_load = "/Users/petr/Desktop/Data_School/python/python-challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv"
file_analysis = "/Users/petr/Desktop/Data_School/python/python-challenge/PyBank/Analysis/budget_analysis.txt"

# Set Variables
total_months = 0
total_profit_loss = 0
netmonthlyaverage = 0

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

        # Set Variable
        monthpnl = int(row[1])

        # Calculate the totals
        total_months += 1
        total_profit_loss += monthpnl

        # Keep track of changes
        profit_loss_change = monthpnl - prev_profit_loss
        

         # Reset Profit/Losses value
        prev_profit_loss = monthpnl
   

         # Identify the greatest increase
        if (profit_loss_change > greatest_increase[1]):
            greatest_increase[1] = profit_loss_change
            greatest_increase[0] = row[0]

        if (profit_loss_change < greatest_decrease[1]):
            greatest_decrease[1] = profit_loss_change
            greatest_decrease[0] = row[0]

         # Add to the profit_loss_change list
            # profit_loss_change.(monthpnl)
        
        # Set Profit/Losses Average
            # profit_loss_avg = sum(profit_loss_change) / len(profit_loss_change)
    

# Show Results
print()
print()
print()
print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(total_months))
print("Total Profit/Losses: " + "$" + str(total_profit_loss))
# print("Average Change: " + "$" + str(round(sum(profit_loss_change) / len(profit_loss_change),2)))
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")

# Show Results in Text
with open(file_analysis, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Profit/Losses: " + "$" + str(total_profit_loss))
    txt_file.write("\n")
    # txt_file.write("Average Change: " + "$" + str(round(sum(profit_loss_change) / len(profit_loss_change),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")