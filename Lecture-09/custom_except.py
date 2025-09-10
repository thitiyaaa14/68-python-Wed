class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Invalid input: {value} is a negative number")

def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError(num)
    else:
        print(f"{num} is a valid position number.")
try:
    number = int(input("Enter a positive number: "))
    check_positive_number(number)
except NegativeNumberError as e:
    print(e)
except ValueError:
    print("Error: Please enter a valid integer.")
finally:
    print("Program execution finished.")