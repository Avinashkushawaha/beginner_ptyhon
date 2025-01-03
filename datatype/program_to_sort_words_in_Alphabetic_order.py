a = "Harry Potter and the Philosopher's Stone"

w = a.split()
print(w)


for i in range (len(w)):
         w[i] = w[i].lower()
         
w.sort()
print(w) 

