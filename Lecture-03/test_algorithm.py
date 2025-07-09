score1 = int(input ("Enter the score for test 1: "))
score2 = int(input ("Enter the score for test 2: "))
score3 = int(input ("Enter the score for test 3: "))
average = (score1 + score2 + score3) / 3
print(f"The average score is {average:.1f}")
if average >= 95:
    print("Congratulation!")
    print("That is a great average!")