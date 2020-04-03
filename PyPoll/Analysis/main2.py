import csv

# Load files
file_load = "/Users/petr/Desktop/Data_School/python/python-challenge/PyPoll/Resources/03-Python_HW_Instructions_PyPoll_Resources_election_data.csv"
poll_analysis = "/Users/petr/Desktop/Data_School/python/python-challenge/PyPank/Analysis/poll_analysis.rtf"

# Set variables
votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}

#read file
with open(file_load,'r') as csvfile: 
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)
    print(csv_header)
