# write a program first file handling
def get_line(file_name: str, num:int):
    file = open(file_name)
    lines = file.readlines()
    line = lines[num-1]
    file.close()
    return line

print(get_line )