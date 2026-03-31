import random

wage_per_hour = 20
full_time = 1
part_time = 2

emp_check = random.choice([0,1,2])

if emp_check == full_time:
    hours = 8
elif emp_check == part_time:
    hours = 4
else:
    hours = 0

daily_wage = wage_per_hour * hours

if emp_check == 1:
    print("Daily wage of full time employee is :",daily_wage)
elif emp_check == 2:
    print("Daily wage of part time employee is :",daily_wage)
else:
    print("Absent")


