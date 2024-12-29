# python program to find Number Divisible by Another Number

print("The numbers divisible by 13 are")
for i in range (1, 100):
    if i % 13 == 0:
        print(i)

# ***********************************
# Solution 2 Using Lambda Function and filter()

l =[39. 48, 26, 98, 33, 76, 87]

result = list(filter(lambda X : X % 13 == 0, l))

print('The numbers divisible numbers')