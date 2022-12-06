from pathlib import Path
# import input text file
# print current path
p = Path(__file__).with_name('input.txt')
count = 0
with p.open('r') as f:
    for line in f:
        # split the line on a comma
        a, b = line.split(',')
        # split each element on a dash
        a1, a2 = a.split('-')
        b1, b2 = b.split('-')        
        #check if element a is within the range of element b
        if int(a1) <= int(b1) and int(a2) >= int(b1):
            count += 1\
        #check if element b is within the range of element a
        elif int(b1) <= int(a1) and int(b2) >= int(a1):
            count += 1
print(count)