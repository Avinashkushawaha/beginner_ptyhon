# Python program to print the multiplication table of a number
# num = int(input("Enter a number: "))
# for i in range(1, 11):
    # print(f"{num} x {i} = {num * i}")
    # print(num, 'x', i, '=', num * i)
    #   print(num, '*', i, '=', num * i)


#   python program to print the entire multiplication table


for i in range(1, 11):
    for j in range(2, 11):
        # print(f"{i} X {j} ", end="\t")
        # print(i,'X', j,'=', i * j,end="\t")
        print(i * j, end="\t")

    print()
        
    
