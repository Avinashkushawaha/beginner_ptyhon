# write a program to get Number of lines and empty and non empty lines from given
def get_lines_info(file_name):
    file = open(file_name)
    total_lines = 0
    valid_lines = 0
    blank_lines = 0
    with open (file_name)as file:
        for line in file:
          total_lines += 1   
        if line.strip() !="":
            valid_lines += 1
        else:
            blank_lines +=1
            return {"total": total_lines,"valid": valid_lines, "blank": blank_lines}    