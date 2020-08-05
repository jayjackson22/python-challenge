#   * The total number of months included in the dataset
#   * The net total amount of "Profit/Losses" over the entire period
#   * The average of the changes in "Profit/Losses" over the entire period
#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period
import csv
import os

path = './Resources/budget_data.csv'

pnl_averages = []
pnl_averages_months = []

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)
    index=0
    #Count
    n=0
    #Profit/Loss
    m=0
    #Starting Value for Greatest Increase
    maxx = -1000000
    #Starting Value for Greatest Decrease
    minn = 1000000
    for row in csv_reader:
        #count of rows
        n=int(n)+1
        #sum of profit/loss
        m=m+int(row[1])
        #profit/loss changes
        #do not send first row of data to array
        if (index==0):
            #define next row's "last row" profit/loss
            x = row[1]
        else:
            #delta between this row and last row
            delta = int(int(row[1])-int(x))
            #new line to array
            pnl_averages_months.append({"Month": row[0], "PnL": row[1], "Delta": delta})
            #new item to list
            pnl_averages.append(delta)
            #find greatest incline and decline
            if (delta>maxx):
                maxx_row = ({"Month": row[0], "PnL": row[1], "Delta": delta})
                maxx = delta
            if (delta<minn):
                minn_row = ({"Month": row[0], "PnL": row[1], "Delta": delta})
                minn = delta
            #define next row's "last row" profit/loss
            x = row[1]
        #next index
        index=index+1

avg_pnl =round(sum(pnl_averages)/len(pnl_averages),2)

print("Financial Analysis")
print("------------------------")
print(f"Total Months: {n}")
print(f"Total: ${m}")
print(f"Average Change: ${avg_pnl}")
print("Greatest Increase in Profits: "+maxx_row["Month"]+" ($"+str(maxx_row["Delta"])+")")
print("Greatest Decrease in Profits: "+minn_row["Month"]+" ($"+str(minn_row["Delta"])+")")

#text string
text_content = ["Financial Analysis\n","------------------------\n",(f"Total Months: {n}\n"),(f"Total: ${m}\n"),(f"Average Change: ${avg_pnl}\n"),("Greatest Increase in Profits: "+maxx_row["Month"]+" ($"+str(maxx_row["Delta"])+")\n"),("Greatest Decrease in Profits: "+minn_row["Month"]+" ($"+str(minn_row["Delta"])+")\n")]

#create file
with open('./Analysis/PyBank Analysis.txt','w') as txt_file:
    txt_file.writelines(text_content)

#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)