#Problem(2) : 
# Assign a message to a variable and then print that message
msg = "Hello World !"
print(msg)

#Problem(3) : 
#  Use a variable to represent your favorite number. Then,
#  using that variable, create a message that reveals your favorite number. Print that message 
num = 21 
print(f"My favorite number is {num}")

#Problem(4) : 
#The volume of a sphere with radius r is 4/3πr3. What is the volume of a sphere 
#with radius 5? Start with a variable named radius and then assign the result to 
#a variable named volume. Display the result. Add comments to indicate 
#that radius is in centimeters and volume in cubic centimeters. 
r = 5 # Radius (r) in centimeters
volume = (4/3)*(22/7)*(r)**3 
# Volume of sphere in  cubic centimeters
print(f"The result of volume is {volume}")

#Problem(5) :
# Let’s your program already contain two integer variables, x and y: 
x ,y = 27,15 
print(f"{x}+{y}={x+y}")
print(f"{x}-{y}={x-y}")
print(f"{x}*{y}={x*y}")
print(f"{x}/{y}={x/y}")

#Problem(6) : 
#Please write a program which asks the user for a number of days. The program 
#then prints out the number of seconds in the number of days given. 
#How many days?
number_of_days=int(input("Enter the number of days ! "))
print(f"The seconds in {number_of_days} is {24*60*60}")

#Problem(7) : 
#Please write a program which asks for the number of students on a course and 
#the desired group size. The program will then print out the number of groups 
#formed from the students on the course. If the division is not even, one of the 
#groups may have fewer members than specified
total_number=int(input("Enter the total number of students ! "))
class_capacity=int(input("Enter the class capacity ! "))

number_of_classes=total_number//class_capacity
number_of_classes+=(total_number//class_capacity) < (total_number/class_capacity)

print(number_of_classes)



