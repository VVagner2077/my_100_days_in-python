


print("Hello to Day 2\n\n")
      
bill = float(input("How much is the bill: $")) 
tip = float(input("How much tip would you like to give? %"))    #inputs
people = int(input("How many people to split the bill? "))

x = ((bill*tip/100)/people)+(bill/people) #count

print(round(x,2)) #it's the print but here I used the round function to round the number and have 2 decimal places