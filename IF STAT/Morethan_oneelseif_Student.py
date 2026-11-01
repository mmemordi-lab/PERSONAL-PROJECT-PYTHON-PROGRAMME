
# PROGRAM TO TEST MORE THAN ONE ELSE IN AN IF STATEMENT 
    
print(" ======== PROGRAM TO TEST MORE THAN ONE ELSE IN AN IF STATEMENT ========== ") 

StudentName = input("Tell us Your Name: ")
    
StudentScore = int(input(" Enter your Student Score: "))

print("=====================")
    
if StudentScore>=70:
   print("Your Name is: ", StudentName)
   print("Your Score has GRADE A category")
  
elif StudentScore >=60:
     print("Your Name is: ", StudentName)
     print("Your Score has GRADE B category")
   
elif StudentScore >=50:
     print("Your Name is: ", StudentName)
     print("Your Score has GRADE C category")
    
else:
     print("Your Name is: ", StudentName)
     print("Your Score is in the FAILED category")