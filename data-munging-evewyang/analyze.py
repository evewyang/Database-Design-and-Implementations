# Place code below to do the analysis part of the assignment.
import csv
with open("data/clean_data.csv", "r") as csvfile:
    lst=[]
    reader = csv.reader(csvfile)
    for line in reader:
        lst.append(line)
    for i in range(1, len(lst)):
        if(i%10==9):
            total=0
            for j in range(i-9, i+1):
                total+=float(lst[j+1][13])
            print("The average temp between " + str(1880+i-9) + " and " + str(1880+i) + " is: " + format((total/10), ".1f"))
