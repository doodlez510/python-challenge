import csv


count=0 
vote_count1=0
vote_count2=0
vote_count3=0
vote_count4=0

csvpath='/Users/doodl/Desktop/UCDSAC201902DATA4/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv' 

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    candidates=["Khan","Correy","Li","O'Tooley"]

    print(f"Header: {csv_header}")

    for row in csvreader:

        count=count+1
        if row[2]==candidates[0]:
            vote_count1=vote_count1+1

        elif row[2]==candidates[1]:
            vote_count2=vote_count2+1

        elif row[2]==candidates[2]:
            vote_count3=vote_count3+1

        else:
            vote_count4=vote_count4+1
if vote_count

percent1=(vote_count1/count)*100
percent2=(vote_count2/count)*100
percent3=(vote_count3/count)*100
percent4=(vote_count4/count)*100

print ("Election Results")
print("---------------------")
print(f"Total votes: {count}")
print(f"{candidates[0]}: {percent1} ({vote_count1})")
print(f"{candidates[1]}: {percent2} ({vote_count2})")
print(f"{candidates[2]}: {percent3} ({vote_count3})")
print(f"{candidates[3]}: {percent4} ({vote_count4})")