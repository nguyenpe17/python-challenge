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

