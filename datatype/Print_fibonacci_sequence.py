# Python Program to Print the Fibonacci sequence
a = 0
b = 1
num = int(input("Enter the number of fibonacci sequence: "))

if num ==  1:
    print(a)
else:
    print(a)
    print(b)
    # for i in range(2, num):
    for i in range(1, num+1):
        c = a + b
        a = b
        b = c
        print(c)      
