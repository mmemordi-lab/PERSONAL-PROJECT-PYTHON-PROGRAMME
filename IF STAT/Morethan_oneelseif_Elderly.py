

# Online Python program to display username and userage 
    
print(" ======== PROGRAM TO TEST MORE THAN ONE ELSE IN AN IF STATEMENT ========== ") 

Username = input("Tell us your Username: ")

UserAge = int(input("Enter your UserAge: "))
print()

print("=====================")
    
if UserAge>=50:
   print("Your Username is: ", Username)
   print("YOU'RE AN ELDERLY PERSON ACCESS GRANTED AND 50% DISCOUNT")
  
elif UserAge >=30:
   print("Your Name is: ", Username)
   print("YOU'RE AN WORKING CLASS PERSON ACCESS GRANTED AND 20% DISCOUNT")
   
elif UserAge >=18:
   print("Your Name is: ", Username)
   print("YOU'RE A YOUNG PERSON ACCESS GRANTED AND 10% DISCOUNT")
    
else:
    print("Your Name is: ", Username)
    print("YOU'RE NOT QUALIFIED TO PARTAKE IN THE SHOW  ACCESS DENIED")