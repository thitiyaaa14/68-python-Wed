work_hours = int (input("Enter the number of hours worked: "))
pay_rate = float (input("Enter the pay rate: "))
if work_hours  > 40:
    overtime = ((work_hours) - 40 *1.5*pay_rate) +(40 * pay_rate)
else : 
    overtime = (work_hours * pay_rate)
print("Overtime pay: $", overtime)