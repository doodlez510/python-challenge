import csv


count=0 
vote_count1=0
vote_count2=0
vote_count3=0
vote_count4=0
winner=""

csvpath='/Users/doodl/Desktop/UCDSAC201902DATA4/03-Python/Homework/Instruction/PyPoll/Resources/election_data.csv' 
file_to_output='/Users/doodl/Desktop/UCDSAC201902DATA4/03-Python/Homework/Instruction/PyPoll/Resources/election_data.txt'
with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    candidates=["Khan","Correy","Li","O'Tooley"]

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

percent1=round((vote_count1/count)*100,2)
percent2=round((vote_count2/count)*100,2)
percent3=round((vote_count3/count)*100,2)
percent4=round((vote_count4/count)*100,2)

if (percent1>percent2) and (percent1>percent3) and (percent1>percent4):
    winner=candidates[0]
elif (percent2>percent1) and (percent2>percent3) and (percent2>percent4):
    winner=candidates[1]
elif (percent3>percent1) and (percent3>percent2) and (percent3>percent4):
    winner=candidates[2]
else:
    winner=candidates[3]
    
    

print ("Election Results")
print("---------------------")
print(f"Total votes: {count}")
print(f"{candidates[0]}: {percent1}% ({vote_count1})")
print(f"{candidates[1]}: {percent2}% ({vote_count2})")
print(f"{candidates[2]}: {percent3}% ({vote_count3})")
print(f"{candidates[3]}: {percent4}% ({vote_count4})")
print(f"Winner is {winner}")

with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("---------------------")
    txt_file.write("\n")
    txt_file.write(f"Total votes: {count}")
    txt_file.write("\n")
    txt_file.write(f"{candidates[0]}: {percent1}% ({vote_count1})")
    txt_file.write("\n")
    txt_file.write(f"{candidates[1]}: {percent2}% ({vote_count2})")
    txt_file.write("\n")
    txt_file.write(f"{candidates[2]}: {percent3}% ({vote_count3})")
    txt_file.write("\n")
    txt_file.write(f"{candidates[3]}: {percent4}% ({vote_count4})")
    txt_file.write("\n")
    txt_file.write(f"Winner is {winner}")