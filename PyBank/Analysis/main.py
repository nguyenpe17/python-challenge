import csv
file = "/Users/petr/Desktop/Data_School/python/python-challenge/PyBank/Resources/03-Python_HW_Instructions_PyBank_Resources_budget_data.csv"
with open(file,'r') as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=",")
    Header = next(csvreader)
    print(Header)