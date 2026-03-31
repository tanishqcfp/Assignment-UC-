import random

wage_per_hour = 20


emp_check = random.choice([0,1,2])

match emp_check:
    case 1:
        emp_type = "full_time"
        hours = 8
    case 2:
        emp_type = "part_time"
        hours = 4
    case _:
        emp_type = "Absent"
        hours = 0

daily_wage = wage_per_hour * hours

print(f"Daily wage of {emp_type} employee is : {daily_wage}")