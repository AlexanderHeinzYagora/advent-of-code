import re
from mergedeep import merge

with open("day07-alex.txt") as f:
    day07 = f.readlines()

day07 = [l.strip('\n\r') for l in day07]

def has_numbers(string):
    """ function to check if string has numbers """
    return any(i.isdigit() for i in string)

#### Description of the approach --------------------------
# first we want to reconstruct the folder tree and map the sizes to the files or the subfolders to the folders
# so we go through each line, and create a folder path if the line starts with "cd"
# and we add a subfolder to the path if the cd is not a ".." (or we shorten the path if it is "..")
# next, we check if the line has numbers (for file sizes)
# if there is a number, we map the size to the file
# then we go backwards in the folder structure (that is, reversed(path)),
# to update the `folder_tree` variable with the complete path
# (not sure if this step could be simplified or if I could avoid the for loop here)
# finally, we merge the current final_tree dictionary with that path.
# this way, we get the folder structure by merging many dictionarys which all lead to files with file sizes
###########################################################
path = []
final_tree = {}
for line in day07:
    if bool(re.search("\$ cd", line)):
        folder = re.findall("\$ cd (.*)", line)[0]
        if folder == "..":
            path = path[:-1]
        else:
            path = path+[folder]

    if has_numbers(line):
        size = re.findall(r"\d+", line)[0]
        file_name = "".join(re.findall(r"[\D+]", line)).strip()

        folder_tree = {file_name: int(size)}
        for key in reversed(path):
            folder_tree = {key:folder_tree} 

        final_tree = merge(final_tree, folder_tree)

final_tree 

# finally, we want to get the sum of all sub-directory file sizes
# so we can create a recursive sum of all nested dictionary values
def recursive_sum(n):
    current_sum = 0
    for key in n:
        if not isinstance(n[key], dict) :
            if  not isinstance(n[key], str) :
                current_sum = current_sum + n[key]
        else: 
            current_sum = current_sum + recursive_sum(n[key])
    return current_sum

# now we want to get the recursive sum for all keys in the dictionaries (also the sub-dictionaries)
def get_all_keys(d):
    for key, value in d.items():
        if not bool(re.search("\.", key)): # this might be redundant, I thought all files have dots...
            if isinstance(value, dict):
                res = recursive_sum(d[key])
                yield key, res
        if isinstance(value, dict):
            yield from get_all_keys(value)

# get the final sum of all directories with sizes less than 100000
final_sum = 0
for x in get_all_keys(final_tree):
    if x[1] < 100000:
        final_sum += x[1]

print("Solution Part 1:", final_sum) # solution part 1

#### PART 2: ------------------------------------------------

# we can also use the recursive sum function to get the total size of the final tree
total_size = recursive_sum(final_tree)
total_space = 70000000
target_space = 30000000
unused_space = total_space-total_size
to_be_deleted = target_space-unused_space

# we can get a dictionary of all files that are larger than to_be_deleted
# then get the smallest
space_dict = {}
for x in get_all_keys(final_tree):
    space_deletion = x[1]
    if space_deletion > to_be_deleted:
        space_dict[space_deletion] = x[0]

minimum_value = min(space_dict.keys())

print("Solution part 2:", minimum_value)
