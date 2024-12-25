# # python program to find the factorial of a number
# num = int(input("Enter a number: "))
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# if num == 0:
#     print("The factorial of 0 is 1")
# if num > 0:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print(f"The factorial of {num} is {factorial}")        


# Using recursion to find the factorial of a number

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorials given number is ",result)
