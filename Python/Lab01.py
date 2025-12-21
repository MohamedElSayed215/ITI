#(2) 
msg = "Hello World !"
print(msg)

#(3)  
num = 21 
print(f"My favorite number is {num}")

#(4)
r = 5 # Radius (r) in centimeters
volume = (4/3)*(22/7)*(r)**3 
# Volume of sphere in  cubic centimeters
print(f"The result of volume is {volume}")

#(5)
x ,y = 27,15 
print(f"{x}+{y}={x+y}")
print(f"{x}-{y}={x-y}")
print(f"{x}*{y}={x*y}")
print(f"{x}/{y}={x/y}")

#(6)
#number_of_days=int(input("Enter the number of days ! "))
#print(f"The seconds in {number_of_days} is {24*60*60}")

#(7)
total_number=int(input("Enter the total number of students ! "))
class_capacity=int(input("Enter the class capacity ! "))

number_of_classes=total_number//class_capacity
number_of_classes+=(total_number//class_capacity) < (total_number/class_capacity)

print(number_of_classes)



