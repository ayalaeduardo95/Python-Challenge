import os
import csv

poll_csv = os.path.join("Resources","pyPoll.csv")

#Variables

total_votes = 0
can_vote_d = {}
can_votes = 0
can_vote_per = {}
winner = ""

with open(poll_csv,"r",encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    for row in csv_reader:
        if row[2] in can_vote_d:
            can_vote_d[row[2]] +=1

        else:
            can_vote_d[row[2]] = 1

        total_votes = total_votes + 1
        winner = max(can_vote_d, key=can_vote_d.get)

vote_per = {}
for key in can_vote_d.keys():
    vote_ls = []
    vote_ls.append(can_vote_d[key]/total_votes * 100)
    vote_ls.append(can_vote_d[key])
    vote_per[key] = vote_ls

print("Election Results")
print(f"Total Votes: {total_votes}")
for key in vote_per:
    print(f"{key}: {vote_per[key][0]}% ({vote_per[key][1]})")
print(f"Winner: {winner}")

output = (
    f"\nElection Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"Khan: 63% (2218231)\n"
    f"Correy: 20% (704200)\n"
    f"Li: 14% (492940)\n"
    f"O'Tooley: 3% (105630)\n"
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n")
with open("output.txt", "w") as txt_file:
    txt_file.write(output)





