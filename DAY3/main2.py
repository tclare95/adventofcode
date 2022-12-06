from pathlib import Path
# import input text file
# print current path
p = Path(__file__).with_name('input.txt')
sum = 0 
with p.open('r') as f:
    # read 3 lines at a time from the input file, and store them in a list
    count = 0
    list_1 = []
    list_2 = []
    list_3 = []
    while count < 300:
        list_1 = f.readline()
        list_2 = f.readline()
        list_3 = f.readline()
        for element in list_1:
            if element in list_2 and element in list_3:
                
                if element.isupper():
                    sum += ord(element)-38
                else:
                   sum += ord(element)-96
                break
        count += 1

print(sum)