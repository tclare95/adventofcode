from pathlib import Path
# import input text file
# print current path
p = Path(__file__).with_name('input.txt') # final
#p = Path(__file__).with_name('test.txt') # proving

def check_list_members (list):
    # check if all of the characters in a list are unique. If they are, return True, else return False
    for i in list:
        if list.count(i) > 1:
            return False
    return True

length = 14 # change this for the length of the string that is being looked for

with p.open('r') as f:
    # read the first line 
    line = f.readline()
    index = 1
    char_list = []
    for char in line:
        # read characters from the line into char_list, until char_list is 4 characters long. If it is 4 characters long, pop the first character and append the new character.
        # if at any point the list is made of 4 different characters, break the loop and return the index

        if len(char_list) < length:
            char_list.append(char)
        else:
            char_list.pop(0)
            char_list.append(char)
        if len(set(char_list)) == length and check_list_members(char_list):
            print(char_list , index)
            break
        index += 1