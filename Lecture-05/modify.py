counter = 0
def increment():
    global counter
    counter += 1
increment()
increment()
print(counter)