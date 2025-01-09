# write a program to generate even numbers using yield keyword

def even_num_gen():
    num = 0
    while True:
        yield num
        num += 2