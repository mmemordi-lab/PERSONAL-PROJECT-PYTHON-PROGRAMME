
# C PROGRANNE TO SHOW ARITHMETIC OPERATORS AND AVERAGE 

print("====== PROGRAM TO TEST ARITHMETIC OPERATORS AND AVERAGE ======")
Name = input("Enter your name: ") 

ComputerScore = int(input("Enter your Computer Score: "))

MathScore = int(input("Enter your Maths Score: "))

EnglishScore = int(input("Enter your English Score: "))

AVERAGE = (MathScore + EnglishScore + ComputerScore) / 3.0

print("========== FINAL RESULT ==============")

print("Your Name is: ", Name)
print(f"Your Average Score is: , {AVERAGE:.2f}")