from pathlib import Path
# import input text file
# print current path
p = Path(__file__).with_name('input.txt')
sum = 0 
with p.open('r') as f:
    for line in f:
        # find the length of the line
        line_length = len(line)-1   
        a = line[0:line_length//2]
        b = line[line_length//2:line_length]
        for element in a:
            if element in b:
                # if element is uppercase, do the uppercase conversion, else do the lowercase conversion
                if element.isupper():
                    sum += ord(element)-38
                else:
                   sum += ord(element)-96
                break
print(sum)