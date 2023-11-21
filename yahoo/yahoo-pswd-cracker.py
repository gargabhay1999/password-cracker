# read the file starting from a particular line
# split the lines based on ':'
# print email and password

with open('password.file', 'r', encoding='ISO-8859-1') as file:
    lines = file.readlines()

start_line_number = 3073
count=0
with open('yahoo-output.txt', 'w', encoding='utf-8') as output:
    for line in lines[start_line_number - 1:-17]:
        parts = line.strip().split(':')
        if(len(parts)==3):
            count+=1
            output.write(f"{parts[1]} : {parts[2]}\n")
        if count==100:
            break