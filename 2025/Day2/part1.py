"""
There is a database of product ID ranges that have been messed up!
Most have been fixed, but there are still some left.

Product IDs appear as a comma separated list (on one line) with each range separated
    by a hyphen (firstID - lastID)

An invalid IDs is any ID which is made of only some sequence of digits repeated twice.
For example, `55` has 5 twice. `123123` has 123 twice.

IDs will not start with a 0 (0101 is not an ID), so `101` is valid

Find all invalid IDs
Note: You must search the whole range

The answer is the sum of all invalid IDs
"""

## Since an invalid ID has the same sequence repeated twice
## Split the id in half and compare the halves for equality
def hasRepeatingSubsequence(id : int) -> bool:
    idStr = str(id)
    mid = len(idStr) // 2

    return idStr[:mid] == idStr[mid:]

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