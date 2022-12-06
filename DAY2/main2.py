from pathlib import Path
# import input text file
# print current path
p = Path(__file__).with_name('input.txt')

final_score = 0

my_options = {
    "X": -1,
    "Y": 0,
    "Z": 1
}

number_convert = {
    "X": 0,
    "Y": 1,
    "Z": 2,
    "A": 0,
    "B": 1,
    "C": 2
}
def calc_outcome(p1, p2):
    if (p1 + 1) % 3 == p2:
        return 1
    elif p1 == p2:
        return 0
    else:
        return -1



# read row of file input.txt
with p.open('r') as f:
    for line in f:
        score = 0
        # split the line into two options
        a, b = line.split()
        print (a, b)
        # give a number to each option
        num_a = number_convert[a]
        # calculate the required outcome
        outcome = my_options[b] # -1 loss, 0 draw, 1 draw
        # calculate the move required to get the outcome 
        # add to score based on outcome
        if outcome == 1:
            score += 6
        elif outcome == 0:
            score += 3
        poss_outcomes = [calc_outcome(num_a, 0), calc_outcome(num_a, 1), calc_outcome(num_a, 2)]
        print(poss_outcomes)
        # select the value from the list that is closest to the required outcome 
        if poss_outcomes[0] == outcome:
            move = "A"
            score += 1
        elif poss_outcomes[1] == outcome:
            move = "B"
            score += 2
        elif poss_outcomes[2] == outcome:
            move = "C"
            score += 3
        final_score += score
        print(a, b, outcome, move, score)


print(final_score)
