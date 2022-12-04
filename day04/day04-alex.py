
with open("day04-alex.txt") as f:
    day04 = f.readlines()

day04 = [l.strip('\n\r') for l in day04]

# get the right format
def get_numbers(input):
    out = ''.join(' ' if not ch.isdigit() else ch for ch in input).strip()
    out = out.split()
    out = list(map(int, out))
    return out

day04 = list(map(get_numbers, day04))


def fully_contain_check(x1, x2, y1, y2):
    one_in_two = all(item in list(range(x1, x2+1)) for item in list(range(y1, y2+1)))     # y+1 because range() does not include the upper number
    two_in_one = all(item in list(range(y1, y2+1)) for item in list(range(x1, x2+1)))
    return any([one_in_two, two_in_one])

sum([fully_contain_check(day04[row][0], day04[row][1], day04[row][2], day04[row][3]) for row in range(len(day04))]) # result part 1


### Part 02 ---------------------------------------

def is_overlapping(x1,x2,y1,y2):
    return max(x1,y1) <= min(x2,y2)

sum([is_overlapping(day04[row][0], day04[row][1], day04[row][2], day04[row][3]) for row in range(len(day04))]) # result part 2


