#required modules,
    import os
    import csv
    
#set variables
    month_counter = 0
    sum_revenue = 0
    sum_revenue_change = 0
    
#connect to data file
    budget_dataCSV = os.path.join('budget_data.csv')
    open data file
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
#months
    month_counter = month_counter + 1
    revenue = float(line[1])
   
#revenue total
    sum_revenue = sum_revenue + revenue
    
#MoM change
    revenue_change = revenue - previous_revenue
    
#Add change in revenue to net change in
    sum_revenue_change = sum_revenue_change + revenue_change
    
#greatest increase and decrease
    "            if revenue_change > max_revenue:
    "                max_month = line[0]
    "                max_revenue = revenue_change
    "\n",
    "            elif revenue_change < min_revenue:\n",
    "                min_month = line[0]\n",
    "                min_revenue = revenue_change\n",
    " \n",
    "            previous_revenue = revenue\n",
    "\n",
    "#avg revenue change\n",
    "        average_revenue = sum_revenue/month_counter\n",
    "        average_revenue_change = sum_revenue_change/(month_counter-1)\n",
    "\n",
    "#rounding results\n",
    "        sum_revenue = int(sum_revenue)\n",
    "        average_revenue_change = float(average_revenue_change)\n",
    "        max_revenue = int(max_revenue)\n",
    "        min_revenue = int(min_revenue)\n",
    "        \n",
    "#terminal results\n",
    "        print(f\"Financial Analysis:\")\n",
    "        print(\"-------------------------------------------------------\")\n",
    "        print(f\"Total Months: {month_counter}\")\n",
    "        print(f\"Total Revenue: ${sum_revenue}\")\n",
    "        print(f\"Average Revenue Change: {average_revenue_change:.2f}\")\n",
    "        print(f\"Greatest Increase in Revenue: {max_month} (${max_revenue})\")\n",
    "        print(f\"Greatest Decrease in Revenue: {min_month} (${min_revenue})\")\n",
    "        print(\"\")\n",
    "        \n",
    "#file results\n",
    "        output_file = budget_dataCSV[0:-4]\n",
    "        write_budget_dataCSV = f\"pybank_results.txt\"\n",
    "        filewriter = open(write_budget_dataCSV, mode = 'w', encoding='utf-8')\n",
    "        filewriter.write(f\"Financial Analysis:\\n\")\n",
    "        filewriter.write(\"-------------------------------------------------------\\n\")\n",
    "        filewriter.write(f\"Total Months: {month_counter}\\n\")\n",
    "        filewriter.write(f\"Total Revenue: ${sum_revenue}\\n\")\n",
    "        filewriter.write(f\"Average Revenue Change: {average_revenue_change:.2f}\\n\")\n",
    "        filewriter.write(f\"Greatest Increase in Revenue: {max_month} (${max_revenue})\\n\")\n",
    "        filewriter.write(f\"Greatest Decrease in Revenue: {min_month} (${min_revenue})\\n\")\n",
    "        filewriter.write(\"\")\n",
    "        filewriter.close()
