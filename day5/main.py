from pathlib import Path
import re
# import input text file
# print current path
p = Path(__file__).with_name('input.txt')

def process_instruction(str, data_array):
    #takes the instruction string and the data array, performs the move and returns the new data array
    # pull the instruction numbers from the string. Position 5 is the number of items to move, position 12 is the source position, position 17 is the destination position
    pos1, pos2, pos3 =  re.findall(r'\d+', str)
    num_items = int(pos1)
    source = int(pos2)-1
    dest = int(pos3)-1

    # produce a range from number of items
    num_range = list(range(num_items))

    for i in num_range:
        # pop the last item from the source position
        items = data_array[source][1].pop()
        # insert the item at the destination position
        data_array[dest][1].append(items)
    
    return data_array

with p.open('r') as f:
    # read the file
    formatted_lines = []
    lines = f.readlines()
    for line in lines:
        formatted_lines.append(line.replace('\n', ''))
    # find the index of the blank list
    blank_index = formatted_lines.index('')
    # split the list into two lists on the blank index
    list1 = formatted_lines[:blank_index]
    list2 = formatted_lines[blank_index+1:]
    # pop the last element of list1, it will be the headers of the list of lists
    headers = list1.pop()
    # split the headers on spaces, and strip the whitespace. if the header is empty, remove it
    data_array = [[header.strip(), []] for header in headers.split(' ') if header != '']
    
    

    for item in reversed(list1):
        # for each item in the list, look in position 1, 5 and 9. If the position is not empty, append it to to data_array in the correct position. This will need to be expan
        #ded if the input file changes
        if item[1] != ' ':
            data_array[0][1].append(item[1])
        if item[5] != ' ':
            data_array[1][1].append(item[5])
        if item[9] != ' ':
            data_array[2][1].append(item[9])
        if item[13] != ' ':
            data_array[3][1].append(item[13])
        if item[17] != ' ':
            data_array[4][1].append(item[17])
        if item[21] != ' ': 
            data_array[5][1].append(item[21])
        if item[25] != ' ': 
            data_array[6][1].append(item[25])
        if item[29] != ' ': 
            data_array[7][1].append(item[29])
        if item[33] != ' ': 
            data_array[8][1].append(item[33])

    
    for instruction in list2:
       data_array = process_instruction(instruction, data_array)

        



    # print(data_array)
    # print the last item from each of the data_array lists
    response_string = ''
    for item in data_array:
       response_string += item[1][-1]

    print(response_string)