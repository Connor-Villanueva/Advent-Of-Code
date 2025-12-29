"""
There is a database of product ID ranges that have been messed up!
Most have been fixed, but there are still some left.

Product IDs appear as a comma separated list (on one line) with each range separated
    by a hyphen (firstID - lastID)

~~An invalid ID is any ID which is made of only some sequence of digits repeated twice.~~
You realize this is wrong. An invalid ID is any ID which is made of only some sequence of digits
repeated AT LEAST twice

For example, `55` has 5 twice. `123123123` has 123 three times. 

IDs will not start with a 0 (0101 is not an ID), so `101` is valid

Find all invalid IDs
Note: You must search the whole range

The answer is the sum of all invalid IDs
"""

## Append the string onto itself
## Remove the first and last characters
##      This is to remove the guarantee that the original string is still in
##      ex) 1231_1231 -> Still has original string so would be True
##      ex) x231_123x -> Removing these characters now gives False
## Check if the original string is in this new string
def hasRepeatingSubsequence(id : int) -> bool:
    idStr = str(id)
    
    doubled = idStr + idStr
    return idStr in doubled[1:-1]

# 123123
# 23123_12312


with open("input", "r") as f:
    data = f.read()

ranges = data.split(",")

invalidIDs = []

for r in ranges:
    ids = r.split("-")

    startID = int(ids[0])
    endID = int(ids[1])

    for id in range(startID, endID + 1):
        if (hasRepeatingSubsequence(id)):
            invalidIDs.append(id)

sum = sum(id for id in invalidIDs)
print(f"Sum of invalid IDs is: {sum}")