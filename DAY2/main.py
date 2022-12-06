from pathlib import Path
# import input text file
# print current path
p = Path(__file__).with_name('input.txt')

final_score = 0

my_options = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

number_convert = {
    "X": 0,
    "Y": 1,
    "Z": 2,
    "A": 0,
    "B": 1,
    "C": 2
}
def winner(p1, p2):
    if (p1 + 1) % 3 == p2:
        return 6
    elif p1 == p2:
        return 3
    else:
        return 0

def calculate_row_score(a, b):
    # calculates rock paper scissors score
    score_to_return = 0
    # look up the score for the second option, as independent of outcome
    score_to_return += my_options[b]
    print(score_to_return)
    #convert the first option to a number - 0, 1, 2
    a = number_convert[a]
    #convert the second option to a number - 0, 1, 2
    b = number_convert[b]
    # calculate the winner
    score_to_return += winner(a, b)
    return score_to_return





# read row of file input.txt
with p.open('r') as f:
    for line in f:
        # split the line into two options
        a, b = line.split()
        print (a, b)
        # calculate the score for the row
        score = calculate_row_score(a, b)
        # print the score
        final_score += score

print(final_score)
