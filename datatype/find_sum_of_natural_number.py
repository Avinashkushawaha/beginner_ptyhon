def Nnum(n):
   if n <= 1:
      return n
   else:
      return (n)+Nnum(n-1) 
n = int(input("Enter a number here :"))

if n <=0:
   print("Enter a positive number:")
else:
   print("The sum of natural number upto given number is",Nnum(n))   