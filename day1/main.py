
# advent of code day 1
from pathlib import Path
# import input text file
# print current path
p = Path(__file__).with_name('input.txt')
elf_list = []
with p.open('r') as f:
    #set a temp variable to 0 to store the sum
    temp = 0
    # add the value of each line to the temp variable
    # read input file until a blank line is found
    # add the temp variable to the elf_list
    for line in f:
        
        if line == '\n':
            elf_list.append(temp)
            temp = 0
        else:
            temp += int(line)
    # add the last temp variable to the elf_list
    elf_list.append(temp)

# print the elf_list
# print(elf_list)
elf_list.sort(reverse=True)
print(elf_list)
