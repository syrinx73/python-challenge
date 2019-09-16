# %%
#connect to modules
import os
import csv

#build variables
month_counter = 0
sum_revenue = 0
sum_revenue_change = 0

# Loop through files
#for files in budget_data:
# Get CSV
budget_dataCSV = os.path.join('budget_data.csv')

#open data file
with open(budget_dataCSV) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        next(csvReader, None)
        line = next(csvReader,None)
        max_month = line[0]
        min_month = line[0]
        revenue = float(line[1])
        min_revenue = revenue
        max_revenue = revenue
        previous_revenue = revenue
        month_counter = 1
        sum_revenue = float(line[1])
        sum_revenue_change = 0

#loop
        for line in csvReader:

# Increase counter for number of months in dataset
            month_counter = month_counter + 1

            revenue = float(line[1])

#total revenue
            sum_revenue = sum_revenue + revenue

#Mom change
            revenue_change = revenue - previous_revenue

            sum_revenue_change = sum_revenue_change + revenue_change

#greatest increase and decrease
            if revenue_change > max_revenue:
                max_month = line[0]
                max_revenue = revenue_change

            if revenue_change < min_revenue:
                min_month = line[0]
                min_revenue = revenue_change

            previous_revenue = revenue

        average_revenue = sum_revenue/month_counter
        average_revenue_change = sum_revenue_change/(month_counter-1)
        sum_revenue = int(sum_revenue)
        average_revenue_change = float(average_revenue_change)
        max_revenue = int(max_revenue)
        min_revenue = int(min_revenue)
        
#terminal results
        print(f"Financial Analysis:")
        print("-------------------------------------------------------")
        print(f"Total Months: {month_counter}")
        print(f"Total Revenue: ${sum_revenue}")
        print(f"Average Revenue Change: ${average_revenue_change:.2f}")
        print(f"Greatest Increase in Revenue: {max_month} (${max_revenue})")
        print(f"Greatest Decrease in Revenue: {min_month} (${min_revenue})")
        print("")
        
#file results
        output_file = budget_dataCSV[0:-4]
        write_budget_dataCSV = f"pybank_results.txt"
        filewriter = open(write_budget_dataCSV, mode = 'w')
        filewriter.write(f"Financial Analysis:\n")
        filewriter.write("-------------------------------------------------------\n")
        filewriter.write(f"Total Months: {month_counter}\n")
        filewriter.write(f"Total Revenue: ${sum_revenue}\n")
        filewriter.write(f"Average Revenue Change: ${average_revenue_change:.2f}\n")
        filewriter.write(f"Greatest Increase in Revenue: {max_month} (${max_revenue})\n")
        filewriter.write(f"Greatest Decrease in Revenue: {min_month} (${min_revenue})\n")
        filewriter.write("")
        filewriter.close()

# %%
