try:
    value = int(input("Enter a integer:  "))
    result = 10 / value 
    print(f"Result is {result}")
except ValueError:
    print("Invalid input! Please enter a integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("End of program")