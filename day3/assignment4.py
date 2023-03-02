grade = int(input("Enter your grade \n"))
if grade < 50:
    print ("You failed the course")
elif grade >= 50 and  grade <= 59 :
    print ("You barely passed the course")
elif grade >= 60 and grade <=  79 : 
    print ("You passed the course")  
elif grade >= 80 and grade <= 89 :
    print ("You did well in this course")
elif grade >= 90:
    print ("You excelled in the course")    


name = (input ("Enter your name ? \n"))
age  = int(input("how old are you ? \n"))
if age <18 :
    print("You are not old enough to use this app")
elif  age >= 18 and age <= 65 :
    print ("Welcome, {name}!")
else:
    print ("Hello, {name}! How can we assist you today")       
