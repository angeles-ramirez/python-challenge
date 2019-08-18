import csv
import os
from pathlib import Path
# need path defined 1st
input_file = Path("Resources", "budget_data.csv")
#define what you're looking for first
sum_months = []
total_profit = []
monthly_profit_change = []
#open csv & read file

with open(input_file,newline="", encoding="utf-8") as budget:
    #file will be labeled budget starting in the above line
    csv_reader = csv.reader(budget, delimiter="," )

    #read/recognize first rows as headers
    header = next(csv_reader)

    avg_mon_profit = (sum(monthly_profit_change)/len(monthly_profit_change))

    
    for row in csv_reader:
        sum_months.append(row[0])
        #print(sum_months)
        total_profit.append(int(row[1]))
        #print(total_profit)

    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        print(monthly_profit_change)

        max_increase_value = max(monthly_profit_change)
        max_decrease_value = min(monthly_profit_change)


        max_inc_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
        max_dec_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 



print("Financial Analysis")
print(" ----------------------------")
print(f"Total Months: {len(sum_months)}")
print(f"Total: $ {sum(total_profit)}")
print(f"Average Change: ${round((avg_mon_profit), 2)}")
print(f"Greatest Increase in Profits: {total_profit[max_inc_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_profit[max_dec_month]} (${(str(max_decrease_value))})")

        
with open("Financial_Analysis_Summary.txt",'w+') as file:

    file.write("Financial Analysis")
    file.write(" ----------------------------")
    file.write(f"Total Months: {len(sum_months)}")
    file.write(f"Total: $ {sum(total_profit)}")
    file.write(f"Average Change: ${round((avg_mon_profit), 2)}")
    file.write(f"Greatest Increase in Profits: {total_profit[max_inc_month]} (${(str(max_increase_value))})")
    file.write(f"Greatest Decrease in Profits: {total_profit[max_dec_month]} (${(str(max_decrease_value))})")
