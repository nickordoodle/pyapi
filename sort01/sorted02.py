#!/usr/bin/env python3
iplist = ['10.8.2.1', '1.1.1.1', '255.255.255.255', '10.1.2.1', '10.2.1.2', \
'10.2.3.2', '10.7.2.1', '192.168.23.1', '192.168.66.1', '10.42.2.1', \
'10.11.10.2', '10.25.32.2', '10.27.21.1', '192.168.55.1']
print('Currently iplist looks like this:', iplist)
print('\nThe results of sorted(iplist) function:', sorted(iplist))
print('\nBut iplist has not actually changed:', iplist)
iplistkeyed = sorted(iplist, key=len)
print('\nResults of sorted(iplist, key=len): ' + str(iplistkeyed))
bakiplistkeyed = sorted(iplist, key=len, reverse=True)
print('\nResults of sorted(iplist, key=len, reverse=True): ' + str(bakiplistkeyed))
# create a custom function for sorting
# the fuction take_second will always return
# what is in the second position
# take the second element for sort
def take_second(secondplacewins):
    return secondplacewins[1]

# random list of tuples
puzzle = [(3, "antelope"), ("Alta", " "), ("Research", "banana", 3.14159265359, "pi")]

# sort list with our custom key take_second
sorted_list = sorted(puzzle, key = take_second)

# print list
print('Sorted list:', sorted_list)


simpsons = [('Moe', "?"), ('Otto', '?'), ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34)]

def byAge(characterbio):
    # isinstance can test if a value is an int, float, str, etc.
    if isinstance(characterbio[1], int):
        return characterbio[1]
    else:
        return 1000  # if a user does not have an age, return 1000
        # which will put them at the end of the list

simpsonsAge = sorted(simpsons, key=byAge)

print('Result of sorted(simpsons, key=byAge): ', simpsonsAge)

