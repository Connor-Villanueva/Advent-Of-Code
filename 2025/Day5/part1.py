"""
You've entered the kitchen, but the elves here have their own problem.
They switched to a new inventory management system and its too complicated.
They can't figure out which ingredients are fresh and which are spoiled.

The database gives a list of fresh ingrediet ID ranges, a blank line, then a list
of avaialable ingredient IDs.

The elves want to know which of the available ingredients are fresh.
You need to figure out how many ingredients are fresh.
"""

def countFreshIngredients(freshRanges : list[tuple[int, int]], available: list[int]):
    count = 0

    for (minID, maxID) in freshRanges:

        for id in available.copy():
            if (minID <= id <= maxID):
                count += 1
                available.remove(id)
    return count

def test():
    with open("test", "r") as f:
        freshRanges = []
        # Get fresh ingredient ID ranges
        while (True):
            line = f.readline().strip()

            if (not line):
                break
            
            minId, maxId = line.split("-")
            freshRanges.append((int(minId), int(maxId)))

        availableIngredients = []
        # Get available ingredient IDs
        while (True):
            line = f.readline().strip()

            if (not line):
                break
            
            availableIngredients.append(int(line))

    print(countFreshIngredients(freshRanges, availableIngredients))

def main():
    with open("input", "r") as f:
        freshRanges = []
        # Get fresh ingredient ID ranges
        while (True):
            line = f.readline().strip()

            if (not line):
                break
            
            minId, maxId = line.split("-")
            freshRanges.append((int(minId), int(maxId)))

        availableIngredients = []
        # Get available ingredient IDs
        while (True):
            line = f.readline().strip()

            if (not line):
                break
            
            availableIngredients.append(int(line))

    print(countFreshIngredients(freshRanges, availableIngredients))


# test()
main()