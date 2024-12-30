# Python program to make a simple Calculator 
num1 = float(input("Enter first  number here :"))
num2 = float(input("Enter second number here :"))

print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplycation \npress 4 is divide")

choice = int(input("Enter your choice from 1-4:"))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)    
elif choice == 3:
    print(num1 * num2)  
elif choice == 4:
    print(num1 / num2)   
else: 
    print("Invalid input")         
            