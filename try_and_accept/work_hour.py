try:
    hour = float(input ("Enter your hour \n "))
    rate = float(input ("enter houtrly rate \n "))
except ValueError: 
    print ("enter a numberic number")   
else:
        
    if  hour > 40 : 
        pay= (hour * rate) * 0.50
        total = (hour * rate) + pay
        print (f"you wworked more than 40 hour your total is{total}")
    else:
        total = hour * rate    
        print(total) 
