try:
    value = int(input("Enter a integer:  "))
    result = 10 / value 
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Result is {result}")

print("End of program")