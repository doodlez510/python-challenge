import csv

count=0
total =0
change=0
profits=[]
max_profit = 0
max_date = ""
min_profit =0
min_date = ""
biggest_difference = 0
smallest_difference= 0
max_profit= 0
prev_profit =0

csvpath= '/Users/doodl/Desktop/UCDSAC201902DATA4/03-Python/Homework/Instruction/PyBank/Resources/budget_data.csv'

with open(csvpath,'r') as csvfile:
    
    csvreader =csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)


    for row in csvreader:
        # [date , profit]
        # 867884
        value=float(row[1])
        
        # filtering max profit
        
        if value > max_profit:  
            max_profit=value
            max_date = (row[0])

        # filtering biggest difference
        # in here we need to skip first iteration
        if(count == 0):
            prev_profit = value

        if biggest_difference < (value - prev_profit):
            biggest_difference = value - prev_profit
            

        if value<min_profit:
            min_profit=value
            min_date= row[0]

        if smallest_difference > value-prev_profit:
            smallest_difference = value-prev_profit

        total=float(row[1])+total
        count=count+1
        
        change = value-prev_profit
        profits.append(change)
    
        prev_profit = value
        average=round(sum(profits)/len(profits),2)

    print("Financial Analysis")
    print("--------------------------")
    print(f"Total months: ${count}")
    print(f"Total: {total}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {max_date} (${biggest_difference})")
    print(f"Greatest Decrease in Profits: {min_date} (${smallest_difference})")
    