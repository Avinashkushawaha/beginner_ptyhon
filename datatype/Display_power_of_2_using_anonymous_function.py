# Python Program to display the power of 2 using anonymous function
nterms = int(input("Enter number of  terms here: "))
result = list(map(lambda x: 2 ** x, range(nterms)))


for i in range(nterms):
    print("2 raised to power", i, "is", result[i])