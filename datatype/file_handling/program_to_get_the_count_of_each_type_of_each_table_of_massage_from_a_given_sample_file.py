# write a program to get the count of each type of each table of massage from a given sample

def get_msg_count(file_name):
    output = {}

    with open(file_name, 'r') as file:
        for line in file:
            if line.strip():
              words = line.split()
              if len(words) > 2:
                msg = words [2]
            if msg in output:
                output[msg] +=1
            else:
                output[msg] = 1
                file.close()

        return output
