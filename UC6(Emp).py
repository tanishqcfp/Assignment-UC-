import random

wage_per_hour = 20
max_hours = 100
max_days = 20

total_salary = 0
total_hours = 0
total_days = 0

while total_hours < max_hours and total_days < max_days:
    total_days += 1
    emp_check = random.choice([0,1,2])

    if emp_check == 1:
        hours = 8
    elif emp_check == 2:
        hours = 4
    else:
        hours = 0
    
    total_hours += hours
    total_salary += hours * wage_per_hour

print("Total Working Days:", total_days)
print("Total Working Hours:", total_hours)
print("Total Monthly Salary:", total_salary)