punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input("Enter anything here: ")  

my_str = " "

for i in string:
    if i not in punc:
        my_str = my_str + i

print(my_str)


