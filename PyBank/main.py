import csv

count=0
total =0
average = 0
max_profit = 0
max_date = ""
min_profit =0
min_date = ""
csvpath= '/Users/doodl/Desktop/UCDSAC201902DATA4/03-Python/Homework/Instructions/PyBank/Resources/budget_data.csv'

with open(csvpath,'r') as csvfile:
    
    csvreader =csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    for row in csvreader:

        value=float(row[1])

        if value>max_profit:
            max_profit=value
            max_date = row[0]

        if value<min_profit:
            min_profit=value
            min_date= row[0]

        total=float(row[1])+total
        count=count+1
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total months: {count}")
    print(f"Total: {total}")
    print(f"Average Change: ${total/count}")
    print(f"Greatest Increase in Profits: {max_date} (${max_profit})")
    print(f"Greatest Decrease in Profits: {min_date} (${min_profit})")