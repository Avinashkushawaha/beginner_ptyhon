#  Write a Python program to read a file and display its contents
with open('example.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()
   
    print(content)
