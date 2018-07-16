#modules
import os
import csv

#path to file
#csvpath = os.path.join("..", "Resources", "budget_data.csv")

#open csv file
with open("budget_data.csv", newline="") as csvfile:
    cvsreader = csv.reader(csvfile, delimiter=",")

    for row in cvsreader:
        print(row)