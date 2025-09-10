try:
    print("start of program")
    x = 1/0 
except ZeroDivisionError as e:
    print(f"Exception message: {e}")

print("end of program")