# write a program to gerate multiples of number using yield keyword
def multiple_gen(num):
    factor = 2
    while True:
        yield num * factor
        
    