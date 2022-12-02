

with open("day02-alex.txt") as f:
    day02 = f.readlines()


day02 = [l.strip('\n\r') for l in day02]


Rock = "A", "X"
Paper = "B", "Y"
Scissors = "C", "Z"


score = 0
for i in day02:
    opponent = i[0]
    me = i[2]
    
    if me in Rock:
        score += 1
    if me in Paper:
        score += 2
    if me in Scissors:
        score += 3

    if opponent in Rock and me in Paper:
        score += 6
    if opponent in Paper and me in Scissors:
        score += 6
    if opponent in Scissors and me in Rock:
        score += 6

    if (opponent, me) in (Rock,  Paper, Scissors):
        score += 3

print(score)


# part 2:

score = 0

for i in day02:
    opponent = i[0]
    me = i[2]
    ## mutate my choice
    # X needs to lose
    if me == "X":
        if opponent in Rock:
            me = "Z"
        if opponent in Scissors:
            me = "Y"
        # if opponent in Paper:
        #     me = "X"
    # Y needs draw
    elif me == "Y":
        if opponent in Rock:
            me = "X"
        if opponent in Scissors:
            me = "Z"
        # if opponent in Paper:
        #     me = "Y"
    # Z needs win
    elif me == "Z":
        if opponent in Rock:
            me = "Y"
        if opponent in Scissors:
            me = "X"
        # if opponent in Paper:
        #     me = "Z"

    # get the points
    if me in Rock:
        score += 1
    if me in Paper:
        score += 2
    if me in Scissors:
        score += 3

    # get the score if you win
    if opponent in Rock and me in Paper:
        score += 6
    if opponent in Paper and me in Scissors:
        score += 6
    if opponent in Scissors and me in Rock:
        score += 6
    # get the score for draw
    if (opponent, me) in (Rock,  Paper, Scissors):
        score += 3

print(score)
