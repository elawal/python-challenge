import csv
data_file = "Resources/budget_data.csv" 
data_analysis = "analysis/budget_analysis.txt"


with open(data_file) as revenue_data:
    reader = csv.reader(revenue_data)
    next(reader)
    row1 = next(reader) 
    total_months = 1
    initial_revenue = int(row1[1])
    month_of_change = []
    revenue_change_list = []
    greatest_increase = [row1[0],int(row1[1])]
    greatest_decrease = [row1[0],int(row1[1])]
    total_revenue = int(row1[1])

    for row in reader: 
        total_months = total_months + 1 
        total_revenue = total_revenue + int(row[1])

        revenue_change = int(row[1]) - initial_revenue
        initial_revenue = int(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row[0]]

        if revenue_change> greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change 


revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

output = (
    f"\nFinancialAnalysis\n"
    f"--------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output) 

with open(data_analysis, "w") as txt_file:
    txt_file.write(output)



