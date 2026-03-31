wage_per_hour = 20
hours = 8
working_days = 20

total_salary = 0

for day in range(working_days):
    total_salary += wage_per_hour * hours

print("Monthly Salary:", total_salary)