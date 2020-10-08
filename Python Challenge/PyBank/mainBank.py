import os
import csv

bank_csv = os.path.join("Resources","pybank.csv")

total_month = 0
month_ls = []
net_ls = []
gi = ["",0]
gd = ["",999999999999999]
total_net = 0

with open(bank_csv,"r",encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)
    first_r = next(csv_reader)
    p_net = int(first_r[1])

    for row in csv_reader:
        total_month = total_month + 1
        total_net = total_net + int(first_r[1])
        net_ch = int(row[1]) - p_net
        p_net = int(row[1])

        net_ls = net_ls + [net_ch]

        if net_ch > gi[1]:
            gi[0] = row[0]
            gi[1] = net_ch
        if net_ch < gd[1]:
            gd[0] = row[0]
            gd[1] = net_ch

net_monthly_avg = sum(net_ls)/len(net_ls)
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${total_net}")
print(f"Average Change: ${net_monthly_avg}")
print(f"Greatest Increase in Profits: {gi[0]} (${gi[1]})")
print(f"Greatest Decrease in Profits: {gd[0]} (${gd[1]})") 

# I don't understand why the Total dosen't match

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------"
    f"Total Months: {total_month}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg}\n"
    f"Greatest Increase in Profits: {gi[0]} (${gi[1]})\n"
    f"Greatest Decrease in Profits: {gd[0]} (${gd[1]})\n")
with open("output.txt", "w") as txt_file:
    txt_file.write(output)








       


   