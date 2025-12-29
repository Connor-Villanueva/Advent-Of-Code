"""
You've entered the kitchen, but the elves here have their own problem.
They switched to a new inventory management system and its too complicated.
They can't figure out which ingredients are fresh and which are spoiled.

The database gives a list of fresh ingrediet ID ranges, a blank line, then a list
of avaialable ingredient IDs.

~~The elves want to know which of the available ingredients are fresh.
You need to figure out how many ingredients are fresh.~~

Now that the elves know what ingredients are fresh, they want to know how many
ingredients in the ranges are fresh.
"""

def countFreshFromRanges(ingredientRanges: list[tuple[int, int]]):
    count = 0

    ingredientRanges.sort(key = lambda x: x[0])

    prevMax = -1
    for minId, maxId in ingredientRanges:
        if maxId <= prevMax:
            continue


        if (minId <= prevMax):
            count += maxId - prevMax
        else:
            count += maxId - minId + 1

        prevMax = maxId

    return count

def test():
    with open("test", "r") as f:
        ingredientRanges = []
        # 
        while (True):
            line = f.readline().strip()

            if (not line):
                break
            
            minID, maxID = line.split("-")
            ingredientRanges.append((int(minID), int(maxID)))

    numFreshIngredients = countFreshFromRanges(ingredientRanges)
    try:
        assert numFreshIngredients == 14
    except AssertionError:
        print(f"Expected 14, Got {numFreshIngredients}")

def main():
    with open("input", "r") as f:
        ingredientRanges = []
        # 
        while (True):
            line = f.readline().strip()

            if (not line):
                break
            
            minID, maxID = line.split("-")
            ingredientRanges.append((int(minID), int(maxID)))

    numFreshIngredients = countFreshFromRanges(ingredientRanges)
    print(numFreshIngredients)

# test()
main()