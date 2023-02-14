x = 100
if x == 100 :
    print ("eqaul to")
    
if x < 90 :
    print ("smaller")

if x > 80 :
    print ("bigger")

print("finish")

#Write a python script that prompts the user for their age, and if they are over 18,
#prints a message saying they are eligible to vote, and if they are under 18, 
#prints a message saying they are not eligible to vote

age = int(input("how old are you?\n"))
if age >= 18:
    print ("eligible to vote")
else: 
    print ("not eligible to vote")    