# Python program to find Armstrong number in an Interval
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

sum = 0
temp = 0

for num in range(lower, upper + 1):
    order = len(str(num))
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)
    sum = 0
    